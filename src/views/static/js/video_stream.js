document.addEventListener('DOMContentLoaded', function() {
  const video = document.getElementById('video');
  const socket = io.connect('http://' + document.domain + ':' + location.port);
  let mediaSource;
  let sourceBuffer;
  let queue = [];
  let isMediaSourceOpen = false;

  function initMediaSource() {
    mediaSource = new MediaSource();
    video.src = URL.createObjectURL(mediaSource);

    mediaSource.addEventListener('sourceopen', function() {
      console.log('MediaSource opened');
      isMediaSourceOpen = true;
      try {
        sourceBuffer = mediaSource.addSourceBuffer('video/webm; codecs="vp8, vorbis"');
        sourceBuffer.addEventListener('updateend', function() {
          if (queue.length > 0 && !sourceBuffer.updating && isMediaSourceOpen) {
            sourceBuffer.appendBuffer(queue.shift());
          }
        });
        // Start requesting video frames once MediaSource is open
        socket.emit('start_stream');
      } catch (e) {
        console.error('Error adding source buffer', e);
      }
    });

    mediaSource.addEventListener('sourceclose', function() {
      console.log('MediaSource closed');
      isMediaSourceOpen = false;
    });

    mediaSource.addEventListener('sourceended', function() {
      console.log('MediaSource ended');
    });

    mediaSource.addEventListener('error', function(e) {
      console.error('MediaSource error', e);
    });
  }

  initMediaSource();

  socket.on('connect', function() {
    console.log('WebSocket connected');
  });

  socket.on('video_frame', function(data) {
    if (!isMediaSourceOpen) {
      console.log('MediaSource is not open, discarding frame');
      return;
    }

    if (sourceBuffer && (sourceBuffer.updating || queue.length > 0)) {
      queue.push(new Uint8Array(data));
    } else if (sourceBuffer) {
      try {
        sourceBuffer.appendBuffer(new Uint8Array(data));
      } catch (e) {
        console.error('Error appending buffer', e);
        // If we get an error here, we might need to re-initialize everything
        isMediaSourceOpen = false;
        queue = [];
        if (mediaSource.readyState === 'open') {
          mediaSource.endOfStream();
        }
        initMediaSource();
      }
    }
  });

  socket.on('disconnect', function() {
    console.log('WebSocket disconnected');
  });

  video.addEventListener('error', function(e) {
    console.error('Video error', e);
  });
});