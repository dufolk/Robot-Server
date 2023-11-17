
$(function () {
    var socketio = io.connect('http://127.0.0.1:8000');
    socketio.on('connect', function () {
        console.log('连接成功');
        socketio.emit('message', {data: 'I\'m connected!'});
    });
    socketio.on('blood', function () {
        console.log('连接成功_blood');
        socketio.emit('blood_msg', {data: 'I\'m connected!'});
    });
    var color_id = {
        0: "RED1",
        1: "RED2",
        2: "BLUE1",
        3: "BLUE2",
    }
    var rankPic = {
        first: '../img/info-img-3.png',
    };
    echarts_1();
    echarts_2();
    map();
    echarts_3();
    echarts_4();
    echarts_5();
    echarts_6();

    function echarts_1() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echarts_1'));

        var data = [
            {value: 12,name: '行业一'},
            {value: 13,name: '行业二'},
            {value: 70,name: '行业三'},
            {value: 52,name: '行业四'},
            {value: 35,name: '行业五'}
        ];

        option = {
            backgroundColor: 'rgba(0,0,0,0)',
            tooltip: {
                trigger: 'item',
                formatter: "{b}: <br/>{c} ({d}%)"
            },
            color: ['#af89d6', '#4ac7f5', '#0089ff', '#f36f8a', '#f5c847'],
            legend: { //图例组件，颜色和名字
                x: '70%',
                y: 'center',
                orient: 'vertical',
                itemGap: 12, //图例每项之间的间隔
                itemWidth: 10,
                itemHeight: 10,
                icon: 'rect',
                data: ['行业一', '行业二', '行业三', '行业四', '行业五'],
                textStyle: {
                    color: [],
                    fontStyle: 'normal',
                    fontFamily: '微软雅黑',
                    fontSize: 12,
                }
            },
            series: [{
                name: '行业占比',
                type: 'pie',
                clockwise: false, //饼图的扇区是否是顺时针排布
                minAngle: 20, //最小的扇区角度（0 ~ 360）
                center: ['35%', '50%'], //饼图的中心（圆心）坐标
                radius: [50, 75], //饼图的半径
                avoidLabelOverlap: true, ////是否启用防止标签重叠
                itemStyle: { //图形样式
                    normal: {
                        borderColor: '#1e2239',
                        borderWidth: 2,
                    },
                },
                label: { //标签的位置
                    normal: {
                        show: true,
                        position: 'inside', //标签的位置
                        formatter: "{d}%",
                        textStyle: {
                            color: '#fff',
                        }
                    },
                    emphasis: {
                        show: true,
                        textStyle: {
                            fontWeight: 'bold'
                        }
                    }
                },
                data: data
            }, {
                name: '',
                type: 'pie',
                clockwise: false,
                silent: true,
                minAngle: 20, //最小的扇区角度（0 ~ 360）
                center: ['35%', '50%'], //饼图的中心（圆心）坐标
                radius: [0, 40], //饼图的半径
                itemStyle: { //图形样式
                    normal: {
                        borderColor: '#1e2239',
                        borderWidth: 1.5,
                        opacity: 0.21,
                    }
                },
                label: { //标签的位置
                    normal: {
                        show: false,
                    }
                },
                data: data
            }]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
    function echarts_2() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echarts_2'));

        option = {
            backgroundColor: 'rgba(0,0,0,0)',
            tooltip: {
                trigger: 'item',
                formatter: "{b}  <br/>{c}辆"
            },
            legend: {
                x: 'center',
                y: '2%',
                data: ['车型一', '车型二', '车型三', '车型四', '车型五'],
                icon: 'circle',
                textStyle: {
                    color: '#fff',
                }
            },
            calculable: true,
            series: [{
                name: '车型',
                type: 'pie',
                //起始角度，支持范围[0, 360]
                startAngle: 0,
                //饼图的半径，数组的第一项是内半径，第二项是外半径
                radius: [41, 110],
                //支持设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
                center: ['50%', '20%'],
                //是否展示成南丁格尔图，通过半径区分数据大小。可选择两种模式：
                // 'radius' 面积展现数据的百分比，半径展现数据的大小。
                //  'area' 所有扇区面积相同，仅通过半径展现数据大小
                roseType: 'area',
                //是否启用防止标签重叠策略，默认开启，圆环图这个例子中需要强制所有标签放在中心位置，可以将该值设为 false。
                avoidLabelOverlap: false,
                label: {
                    normal: {
                        show: true,
                        formatter: '{c}辆'
                    },
                    emphasis: {
                        show: true
                    }
                },
                labelLine: {
                    normal: {
                        show: true,
                        length2: 1,
                    },
                    emphasis: {
                        show: true
                    }
                },
                data: [{
                    value: 600,
                    name: '车型一',
                    itemStyle: {
                        normal: {
                            color: '#f845f1'
                        }
                    }
                },
                    {
                        value: 1100,
                        name: '车型二',
                        itemStyle: {
                            normal: {
                                color: '#ad46f3'
                            }
                        }
                    },
                    {
                        value: 1200,
                        name: '车型三',
                        itemStyle: {
                            normal: {
                                color: '#5045f6'
                            }
                        }
                    },
                    {
                        value: 1300,
                        name: '车型四',
                        itemStyle: {
                            normal: {
                                color: '#4777f5'
                            }
                        }
                    },
                    {
                        value: 1400,
                        name: '车型五',
                        itemStyle: {
                            normal: {
                                color: '#44aff0'
                            }
                        }
                    },

                    {
                        value: 0,
                        name: "",
                        label: {
                            show: false
                        },
                        labelLine: {
                            show: false
                        }
                    },
                    {
                        value: 0,
                        name: "",
                        label: {
                            show: false
                        },
                        labelLine: {
                            show: false
                        }
                    },
                    {
                        value: 0,
                        name: "",
                        label: {
                            show: false
                        },
                        labelLine: {
                            show: false
                        }
                    },
                    {
                        value: 0,
                        name: "",
                        label: {
                            show: false
                        },
                        labelLine: {
                            show: false
                        }
                    },
                    {
                        value: 0,
                        name: "",
                        label: {
                            show: false
                        },
                        labelLine: {
                            show: false
                        }
                    }
                ]
            }]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }

    function map() {
        // 基于准备好的dom，初始化echarts实例
        var chartDom = document.getElementById('map');
        var myChart = echarts.init(chartDom);
        var option;

        option = {
            grid: {
                left: '0%',
                right: '0%',
                top: '0%',
                bottom: '0%',
            },
            title: {
                text: '实时对局状态'
            },
            xAxis: {
                //范围0-800
                min: 0,
                max: 808,
              show: false
            },
            yAxis: {
                //范围0-450
                min: 0,
                max: 448,
              show: false
            },
            series: [
              {
                type: 'effectScatter',
                symbolSize: 20,
                data: [
                  [-15, -15],
                  [-15, -15]
                ],
                color: ['#ff0000']
              },
              {
                type: 'effectScatter',
                symbolSize: 20,
                data: [
                  [-15, -15],
                  [-15, -15]
                ],
                color: ['#0000ff']
              }
            ]
          };


        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        socketio.on('message', function (msg) {
            // console.log(msg);
            // 遍历字典msg，将数据放入option中
            for (var id in msg){
                console.log(id, Math.floor(id/2), id%2)
                var data = msg[id];
                option.series[Math.floor(id/2)].data[id%2] = data;
            }
            myChart.setOption(option); 
        });
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
    function echarts_3() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echarts_3'));
    
        var yData = function() {
            var data = ['红方','蓝方'];
            return data;
        }();
    
        var data = [100,100];
    
        option = {
            tooltip: {
                show: "true",
                trigger: 'item',
                backgroundColor: 'rgba(0,0,0,0.4)',
                padding: [8, 10],
                formatter: function(params) {
                    if (params.seriesName != "") {
                        return params.name + ' :  ' + params.value + ' 血';
                    }
                },
            },
            grid: {
                borderWidth: 0,
                top: 20,
                bottom: 35,
                left: 55,
                right: 30,
                textStyle: {
                    color: "#fff"
                }
            },
            xAxis: {
                type: 'value',
                axisTick: {
                    show: false
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: '#32346c',
                    }
                },
                splitLine: {
                    show: true,
                    lineStyle: {
                        color: '#32346c ',
                    }
                },
                axisLabel: {
                    textStyle: {
                        color: '#bac0c0',
                        fontWeight: 'normal',
                        fontSize: '12',
                    },
                    formatter: '{value}',
                },
            },
            yAxis: {
                type: 'category',
                axisTick: {
                    show: false
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: '#363e83',
                    }
                },
                axisLabel: {
                    inside: false,
                    textStyle: {
                        color: '#bac0c0',
                        fontWeight: 'normal',
                        fontSize: '12',
                    },
                },
                data: yData,
            },
            series: [{
                type: 'bar',
                itemStyle: {
                    normal: {
                        show: true,
                        color: 
                            new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                                offset: 0,
                                color: '#ff7f7f' // 第一个柱子的起始颜色
                            }, {
                                offset: 1,
                                color: '#ff0000' // 第一个柱子的结束颜色
                            }]),
                            // new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                            //     offset: 0,
                            //     color: '#ff0000' // 第二个柱子的起始颜色
                            // }, {
                            //     offset: 1,
                            //     color: '#ff7f7f' // 第二个柱子的结束颜色
                            // }])
                        barBorderRadius: 50,
                        borderWidth: 0,
                    },
                    emphasis: {
                        shadowBlur: 15,
                        shadowColor: 'rgba(105,123, 214, 0.7)'
                    }
                },
                zlevel: 2,
                barWidth: '20%',
                data: data,
            }]
        };
    
        myChart.setOption(option);
        window.addEventListener("resize", function() {
            myChart.resize();
        });
    }
    function echarts_4() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echarts_4'));

        option = {

            tooltip : {
                trigger: 'item',
                formatter: "{b}: <br/>  {c} ({d}%)"
            },

            toolbox: {
                show : false,
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false},
                    magicType : {
                        show: true,
                        type: ['pie', 'funnel']
                    },
                    restore : {show: true},
                    saveAsImage : {show: true}
                }
            },
            calculable : true,
            series : [

                {
                    name:'排名',
                    type:'pie',
                    color: ['#af89d6', '#f5c847', '#ff999a', '#0089ff','#25f3e6'],
                    radius : [20, 100],
                    center : ['50%', '50%'],
                    roseType : 'area',
                    data:[
                        {value:70, name:'NO.4'},
                        {value:90, name:'NO.3'},
                        {value:110, name:'NO.2'},
                        {value:150, name:'NO.1'},
                        {value:40, name:'NO.5'}

                    ]
                }
            ]
        };


        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
    function echarts_5() {
        var myChart = echarts.init(document.getElementById('echarts_5'));
    
        var yData = function() {
            var data = ['red','blue'];
            return data;
        }();
    
        var data = [100,100];
    
        option = {
            tooltip: {
                show: "true",
                trigger: 'item',
                backgroundColor: 'rgba(0,0,0,0.4)',
                padding: [8, 10],
                formatter: function(params) {
                    if (params.seriesName != "") {
                        return params.name + ' :  ' + params.value + ' 血';
                    }
                },
            },
            grid: {
                borderWidth: 0,
                top: 20,
                bottom: 35,
                left: 55,
                right: 30,
                textStyle: {
                    color: "#fff"
                }
            },
            xAxis: {
                type: 'value',
                axisTick: {
                    show: false
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: '#32346c',
                    }
                },
                splitLine: {
                    show: true,
                    lineStyle: {
                        color: '#32346c ',
                    }
                },
                axisLabel: {
                    textStyle: {
                        color: '#bac0c0',
                        fontWeight: 'normal',
                        fontSize: '12',
                    },
                    formatter: '{value}',
                },
            },
            yAxis: {
                type: 'category',
                axisTick: {
                    show: false
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: '#363e83',
                    }
                },
                axisLabel: {
                    inside: false,
                    textStyle: {
                        color: '#bac0c0',
                        fontWeight: 'normal',
                        fontSize: '12',},
                        formatter: function (value) {
                            return '{'+ value + '| }\n{value|' + value + '}';
                     },
                        rich:{
                            red: {
                                height: 20,
                                align: 'center',
                                backgroundColor: {
                                    image: rankPic.first
                                }
                            },
                            blue: {
                                height: 20,
                                align: 'center',
                                backgroundColor: {
                                    image: rankPic.first
                                }
                            },
                        },
                    
                   
                },
                data: yData,
            },
            series: [{
                type: 'bar',
                itemStyle: {
                    normal: {
                        show: true,
                        color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                            offset: 0,
                            color: '#ff7f7f'
                        }, {
                            offset: 1,
                            color: '#ff0000'
                        }]),
                        // color:['#333','#666'],
                        barBorderRadius: 50,
                        borderWidth: 0,
                    },
                    emphasis: {
                        shadowBlur: 15,
                        shadowColor: 'rgba(105,123, 214, 0.7)'
                    }
                },
                zlevel: 2,
                barWidth: '20%',
                data: data,
            }]
        };
    
        myChart.setOption(option);
        socketio.on('blood_message', function (data) {
            for (var robotId in data) {
                var health = data[robotId];
                var seriesIndex = Math.floor(robotId / 2);
                var dataIndex = robotId % 2;
                option.series[seriesIndex].data[dataIndex] = health;
            }
            myChart.setOption(option);
        });
        window.addEventListener("resize",function(){
            myChart.resize();
        });

    }
    function echarts_6() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echarts_6'));

        var data = {
            "chart": [{
                month: "NO.1",
                value: 600,

            },

                {
                    month: "NO.2",
                    value: 500,

                },

                {
                    month: "NO.3",
                    value: 614,

                },

                {
                    month: "NO.4",
                    value: 442,

                },

                {
                    month: "NO.5",
                    value: 322

                }

            ]
        }


        var xAxisMonth = [],
            barData = [],
            lineData = [];
        for (var i = 0; i < data.chart.length; i++) {
            xAxisMonth.push(data.chart[i].month);
            barData.push({
                "name": xAxisMonth[i],
                "value": data.chart[i].value
            });
            lineData.push({
                "name": xAxisMonth[i],
                "value": data.chart[i].ratio
            });
        }

        option = {
            // backgroundColor: "#020d22",
            title: '',
            grid: {
                top: '10%',
                left: '18%',
                bottom: '3%',
                right:'5%',
                containLabel: true
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'none'
                },
                formatter: function(params) {
                    return params[0]["data"].name + "<br/>" + '报警次数: ' + params[1]["data"].value+'次' ;
                }
            },
            xAxis: [{
                type: 'category',
                show: false,
                data: ['NO.1', 'NO.2', 'NO.3', 'NO.4', 'NO.5'],
                axisLabel: {
                    textStyle: {
                        color: '#b6b5ab'
                    }
                }
            },
                {
                    type: 'category',
                    position: "bottom",
                    data: xAxisMonth,
                    boundaryGap: true,
                    // offset: 40,
                    splitLine: {
                        show: false,
                        lineStyle: {
                            color: "rgba(255,255,255,0.2)"
                        }
                    },
                    axisTick: {
                        show: false
                    },
                    axisLine: {
                        show: true,
                        color: "rgba(255,255,255,0.2)"
                    },
                    axisLabel: {
                        textStyle: {
                            color: '#b6b5ab'
                        }
                    }
                }

            ],
            yAxis: [{
                show: true,
                offset: 52,
                splitLine: {
                    show: false,
                    lineStyle: {
                        color: "rgba(255,255,255,0.2)"
                    }
                },
                axisTick: {
                    show: false
                },
                axisLine: {
                    show: true,
                    color: "rgba(255,255,255,0.2)"
                },
                axisLabel: {
                    show: true,
                    color: '#b6b5ab'
                }
            }, {
                show: false,
                type: "value",
                // name: "合格率(%)",
                nameTextStyle: {
                    color: '#ccc'
                },
                axisLabel: {
                    color: '#ccc'
                },
                splitLine: {
                    show: false
                },
                axisLine: {
                    show: true
                },
                axisTick: {
                    show: true
                }
            }],
            color: ['#e54035'],
            series: [{
                name: '训练人次',
                type: 'pictorialBar',
                xAxisIndex: 1,
                barCategoryGap: '-80%',
                // barCategoryGap: '-5%',
                symbol: 'path://d="M150 50 L130 130 L170 130  Z"',
                itemStyle: {
                    normal: {
                        color: function(params) {
                            var colorList = [
                                'rgba(13,177,205,0.8)', 'rgba(29,103,182,0.6)',
                                'rgba(13,177,205,0.8)', 'rgba(29,103,182,0.6)',
                                'rgba(13,177,205,0.8)', 'rgba(29,103,182,0.6)'
                            ];
                            return colorList[params.dataIndex];
                        }
                    },
                    emphasis: {
                        opacity: 1
                    }
                },
                data: barData,
            },
                {
                    symbol: 'image://data:image/png;base64,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',
                    symbolSize: 42,
                    name: "完成率",
                    type: "line",
                    yAxisIndex: 1,
                    data: lineData,
                    itemStyle: {
                        normal: {
                            borderWidth: 5,
                            color: {
                                colorStops: [{
                                    offset: 0,
                                    color: '#821eff'
                                },

                                    {
                                        offset: 1,
                                        color: '#204fff'
                                    }
                                ],
                            }
                        }
                    }
                }
            ]
        }


        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }






})