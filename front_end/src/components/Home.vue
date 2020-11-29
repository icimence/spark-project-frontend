<template>
    <div class="home">
        <div class="header">
            <p style="color: white; font-size: 30px;font-family: STSong">Stackoverflow 检 测 平 台</p>
        </div>
        <div class="main">
            <div class="pum_left">
                <div class="top">
                    <ve-ring :data="roseMapChartData" jude-width=true height="100%"
                             :settings="roseMapChartSetting"></ve-ring>
                </div>
                <div>
                    <div class="bot">
                        <template>
                            <ve-funnel :data="funnelChartData" :settings="funnelChartSettings"
                                       height="350px"></ve-funnel>
                        </template>

                    </div>
                </div>
            </div>
            <div class="main-center">
                <div class="center-top">
                    <ve-heatmap jude-width=true height="100%" :data="worldMapChartData"
                                :settings="worldMapChartSettings"></ve-heatmap>
                </div>
                <div class="center-bottom">
                    <ve-line jude-width=true height="100%" :data="lineChartData" :settings="lineChartSettings" :color="colors" :extend="extend"></ve-line>
                </div>
            </div>
            <div class="pum_right">
                <div class="top">
                    <ve-bar jude-width=true height="100%" :data="barChartData" :settings="barChartSettings"></ve-bar>
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
import WordCloud from "./WordCloud";
import LineChart from "./LineChart";
import RoseMap from "./RoseMap";
import BarChart from "./BarChart";
import MyMap from "./Map";
import Element_ from "./Element";

export default {
    components: {RoseMap, LineChart, BarChart, WordCloud, MyMap, Element_},
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
            metrics: ['C', 'Java','Python'],
            dimension: ['time']
        }
        this.extend = {
            'xAxis.0.axisLabel.rotate': 45
        }
        return {
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
            lineChartData:{
                columns: ['time', 'C','Java','Python'],
                rows: [],
            },
            randomNumber: 0
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
        getLineChartRowsFromBackend(){
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
            }, 2000)
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
    background-color: #082C74;
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
    background-color: #3791EF;
    border-radius: 10px;
    margin: 1% 0.7% 10px 0.6%;


}

.main {
    flex: 1;
    /* height: 400px; */
    display: flex;
    border-bottom: 10px solid #082C74;
}

.pub {
    flex: 1;
}

.pum_left {
//width: 400px; width: 20%; border-radius: 10px;
}

.pum_right {
    width: 400px;
    border-radius: 10px;
}

.top {
    flex: 1;
    border-bottom: 10px solid #082C74;
    background-color: #3791EF;
    border-radius: 10px;

}

.pum_left .top {
    border-bottom: 0;
    height: 50%;
    margin-left: 3%;
    border-radius: 10px;
    background-color: #3791EF;

}

.pum_left .bot {
    border-bottom: 0;
    margin-top: 5%;
    height: 335px;
    border-radius: 10px;
    margin-left: 3%;
    background-color: #3791EF;

}

.pum_right .top {
    border-bottom: 0;
    background-color: #3791EF;
    border-radius: 10px;
    height: 45%;
    margin-right: 3%;
}

.pum_right .bot {
    background-color: #3791EF;
    border-radius: 10px;
    margin-top: 2.5%;
    padding-top: -3.5%;
    margin-right: 3%;
    height: 53.32%;
}

.pum_right .time {
    background-color: #3791EF;
    padding-top: 6%;
    height: 8.9%;
    margin-top: 2.5%;
    margin-right: 3%;
    border-radius: 10px;
}

.main-center {
    border-left: 10px solid #082C74;
    border-right: 10px solid #082C74;
    width: 60%;
}

.main-center .center-top {
    background-color: #3791EF;
    border-radius: 10px;
    height: 58%;
    padding-left: 4%;
}

.main-center .center-bottom {
    margin-top: 1.5%;
    height: 40%;
    background-color: #3791EF;
    border-radius: 10px;
}

.footer {
    height: 150px;
    border: 0;
    display: flex;
    border-bottom: 1px solid #ccc;
}
</style>
