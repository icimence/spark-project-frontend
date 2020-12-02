<template>
    <div class="home">
        <div class="header">
            <img style="margin-top: 1px;zoom: 48%;" src="../assets/title.png" alt="logo"/>
        </div>
        <div class="main">
            <div class="pum_left">
                <div class="top">
                    <ve-ring :data="roseMapChartData" width="100%"
                             :settings="roseMapChartSetting" :loading="this.roseMapLoading"
                             :extend="roseExtend"></ve-ring>
                </div>
                <div>
                    <div class="bot">
                        <template>
                            <ve-funnel :data="funnelChartData" :settings="funnelChartSettings"
                                       height="350px" :extend="funnelExtend"></ve-funnel>
                        </template>

                    </div>
                </div>
            </div>
            <div class="main-center">
                <div class="center-top">
                    <ve-heatmap jude-width=true :data="worldMapChartData"
                                :settings="worldMapChartSettings" height="92%"
                                :extend="worldMapExtend"></ve-heatmap>
                </div>
                <div class="center-bottom">
                    <ve-line jude-width=true height="100%" :data="lineChartData" :settings="lineChartSettings"
                             :color="colors" :extend="extend"></ve-line>
                </div>
            </div>
            <div class="pum_right">
                <div class="top">
                    <ve-bar jude-width=true height="100%" :data="barChartData" :settings="barChartSettings"
                            :extend="barChartExtend"></ve-bar>
                </div>
                <div class="bot">
                    <ve-wordcloud
                        :data="wordCloudChartData"
                        :loading="loading"
                        height="370px"></ve-wordcloud>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import 'v-charts/lib/style.css'

export default {
    data() {
        this.roseMapChartSetting = {
            roseType: 'radius'
        }
        this.worldMapChartSettings = {
            position: 'world',
            type: 'map',
            geo: {
                label: {
                    emphasis: {
                        show: false
                    }
                },
                itemStyle: {
                    normal: {
                        areaColor: '#323c48',
                        borderColor: '#111'
                    },
                    emphasis: {
                        areaColor: '#2a333d'
                    }
                }
            }
        }
        this.barChartSettings = {
            metrics: ['number'],
            dimension: ['language'],
            dataOrder: {
                label: 'number',
                order: 'desc'
            }
        }
        this.funnelChartSettings = {
            useDefaultOrder: true,
            filterZero: true
        }
        this.lineChartSettings = {
            metrics: ['C', 'Java', 'Python'],
            dimension: ['time']
        }
        this.extend = {
            'xAxis.0.axisLabel.rotate': 45,
            legend: {
                show: true,
                textStyle: {
                    color: '#fff'
                }
            },
            xAxis: {
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            },
            yAxis: {
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            }
        }
        this.barChartExtend = {
            legend: {
                show: true,
                textStyle: {
                    color: '#fff'
                }
            },
            xAxis: {
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            },
            yAxis: {
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            }
        }
        this.roseExtend = {
            legend: {
                show: true,
                textStyle: {
                    color: '#fff'
                }
            },
        }
        this.funnelExtend = {
            legend: {
                show: true,
                textStyle: {
                    color: '#fff'
                }
            },
        }
        this.worldMapExtend = {
            legend: {
                show: true,
                textStyle: {
                    color: '#fff'
                }
            },
        }
        return {
            roseMapLoading: true,
            strDate: '',
            strTime: '',
            barChartData: {
                columns: ['number', 'language'],
                rows: []
            },
            roseMapChartData: {
                columns: ['state', 'number'],
                rows: []
            },
            wordCloudChartData: {
                columns: ['word', 'count'],
                rows: []
            },
            worldMapChartData: {
                columns: ['lat', 'lng', 'number'],
                rows: []
            },
            funnelChartData: {
                columns: ['range', 'number'],
                rows: []
            },
            lineChartData: {
                columns: ['time', 'C', 'Java', 'Python'],
                rows: [],
            },
        }
    },
    methods: {
        formatDate() {
            const date = new Date();
            const year = date.getFullYear()
            const month = date.getMonth()
            const day = date.getDate()
            const hour = date.getHours()
            const minutes = date.getMinutes()
            const seconds = date.getSeconds()
            this.strDate = year + "年 " + (month + 1) + "月 " + day + "日"
            this.strTime = hour + ":" + minutes + ":" + seconds
        },
        getLineChartRowsFromBackend() {
            const path = `http://localhost:5000/api/line`
            axios.get(path)
                .then(response => {
                    this.lineChartData.rows = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        getFunnelChartRowsFromBackend() {
            const path = `http://localhost:5000/api/funnel`
            axios.get(path)
                .then(response => {
                    this.funnelChartData.rows = response.data
                    console.log(response.data)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        getWordCloudRowsFromBackend() {
            const path = `http://localhost:5000/api/count`
            axios.get(path)
                .then(response => {
                    this.wordCloudChartData.rows = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        getRoseMapRowsFromBackend() {
            this.roseMapLoading = true
            const path = `http://localhost:5000/api/answer`
            axios.get(path)
                .then(response => {
                    console.log(response.data)
                    this.roseMapChartData.rows = response.data
                    console.log(this.roseMapChartData.rows)
                })
                .catch(error => {
                    console.log(error)
                })
            this.roseMapLoading = false
        },
        getWorldMapRowsFromBackend() {
            const path = `http://localhost:5000/api/location`
            axios.get(path)
                .then(response => {
                    this.worldMapChartData.rows = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        getBarChartRowsFromBackend() {
            const path = `http://localhost:5000/api/barchart`
            axios.get(path)
                .then(response => {
                    this.barChartData.rows = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        times() {
            return setInterval(() => {
                this.getRoseMapRowsFromBackend()
                this.getWordCloudRowsFromBackend()
                this.getWorldMapRowsFromBackend()
                this.getBarChartRowsFromBackend()
                this.getFunnelChartRowsFromBackend()
                this.getLineChartRowsFromBackend()
            }, 5000)
        },
        getClock() {
            return setInterval(() => {
                this.formatDate()
            }, 1000)
        }
    },
    destroyed() {
        clearInterval(this.times())
        clearInterval(this.getClock())
    },
    created() {
        this.getRoseMapRowsFromBackend()
        this.getWordCloudRowsFromBackend()
        this.getWorldMapRowsFromBackend()
        this.getBarChartRowsFromBackend()
        this.getFunnelChartRowsFromBackend()
        this.getLineChartRowsFromBackend()
        this.formatDate()
    },
    mounted() {
        this.times()
        this.getClock()
    }
}
</script>

<style>
.home {
    background-image: url("../assets/background.png");
    height: 100%;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    bottom: 0;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

.header {
    height: 100px;
    line-height: 100px;
    border-radius: 10px;
    margin: 1% 0.7% 10px 0;


}

.header.topImg {
    zoom: 50%;
}

.main {
    flex: 1;
    display: flex;
    margin-bottom: 10px;
}

.pub {
    flex: 1;
}

.pum_left {
    width: 400px;
    border-radius: 10px;
}

.pum_right {
    width: 400px;
    border-radius: 10px;
}

.top {
    flex: 1;
    margin-bottom: 10px;
}

.pum_left .top {
    padding-top: 9%;
    background-image: url("../assets/borderB.png");
    background-size: 100% 100%;
    border-color: whitesmoke;
    height: 50%;
    margin-left: 3%;
    border-radius: 10px;
}

.pum_left .bot {
    padding-left: -5%; padding-top: 6%;
    background-image: url("../assets/borderB.png");
    background-size: 100% 100%;
    border-color: whitesmoke;
    margin-top: 3%;
    height: 300px;
    border-radius: 10px;
    margin-left: 3%;
}

.pum_right .top {
    background-image: url("../assets/borderB.png");
    background-size: 100% 100%;
    height: 45%;
    margin-right: 3%;
    padding-top: 5%;
}

.pum_right .bot {
    background-image: url("../assets/borderD.png"); background-size: 100% 100%;
    margin-top: 2.5%;
    padding-top: -3.5%;
    margin-right: 3%;
    height: 53.32%;
}

.main-center {
    margin-left: 10px;
    margin-right: 10px;
    width: 60%;
}

.main-center .center-top {
    background-image: url("../assets/border.png"); background-size: 100% 100%;
    height: 58%;
    margin-top: -5%;
    padding-left: 4%;
    padding-top: 8%;
}

.main-center .center-bottom {
    background-image: url("../assets/borderE.png"); background-size: 100% 100%;
    padding-top: 8px;
    margin-top: -2%;
    height: 39.7%;

}

</style>
