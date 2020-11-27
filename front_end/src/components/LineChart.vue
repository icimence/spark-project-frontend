<template>
    <ve-line :data="chartData" :settings="chartSettings" :color="colors" ></ve-line>
</template>

<script>
export default {
    name:'LineChart',
    data () {
        this.chartSettings = {
            metrics: ['访问用户'],
            dimension: ['时间'],
            area: true
        }
        return {
            chartData: {
                columns: ['时间', '访问用户'],
                rows: [
                    { '时间': '1/1', '访问用户': 1393 },
                    { '时间': '1/2', '访问用户': 3530 },
                    { '时间': '1/3', '访问用户': 2923 },
                    { '时间': '1/4', '访问用户': 1723 },
                    { '时间': '1/5', '访问用户': 3792 },
                    { '时间': '1/6', '访问用户': 4593 }
                ],
                colors:['red']
            }
        }
    }
}
</script>
