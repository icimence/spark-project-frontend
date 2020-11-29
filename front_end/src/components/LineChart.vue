<template>
    <ve-line jude-width=true height="100%" :data="chartData" :settings="chartSettings" :color="colors" ></ve-line>
</template>

<script>
export default {
    name:'LineChart',
    data () {
        this.chartSettings = {
            metrics: ['C', 'Java','Python'],
            dimension: ['time']
        }
        return {
            chartData: {
                columns: ['time', 'C','Java','Python'],
                rows: [
                    { 'time': '1/1', 'C': 1393,'Java':23423,'Python':234 },
                    { 'time': '1/1', 'C': 1393,'Java':23423,'Python':234 },
                ],
            }
        }
    }
}
</script>
