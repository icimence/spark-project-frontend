<template>
    <ve-bar jude-width=true height="100%" :data="chartData" :settings="chartSettings"></ve-bar>
</template>

<script>
export default {
    name:'BarChart',
    data () {
        this.chartSettings = {
            metrics: ['number'],
            dataOrder: {
                label: 'number',
                order: 'desc'
            }
        }
        return {
            chartData: {
                columns: ['number', 'language'],
                rows: [
                    { 'number': '324234', 'language': 1393, '下单用户': 1093, '下单率': 0.32 },
                    { 'number': '1/2', 'language': 3530, '下单用户': 3230, '下单率': 0.26 },
                    { 'number': '1/3', 'language': 2923, '下单用户': 2623, '下单率': 0.76 },
                    { 'number': '1/4', 'language': 1723, '下单用户': 1423, '下单率': 0.49 },
                    { 'number': '1/5', 'language': 3792, '下单用户': 3492, '下单率': 0.323 },
                    { 'number': '1/6', 'language': 4593, '下单用户': 4293, '下单率': 0.78 }
                ]
            }
        }
    }
}
</script>
