<template>
    <ve-heatmap :data="chartData" :settings="chartSettings"></ve-heatmap>
</template>

<script>
export default {
    name:'Map',
    data () {
        this.chartSettings = {
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
        return {
            chartData: {
                columns: ['lat', 'lng', '人数'],
                rows: [
                    { 'lat': 115.892151, 'lng': 28.6, '人数': 10 },
                    { 'lat': 17.000923, 'lng': 36.675807, '人数': 4 },
                    { 'lat': 113.665412, 'lng': 34.757975, '人数': 8 },
                    { 'lat': 114.298572, 'lng': 0.55, '人数': 2 },
                    { 'lat': 112.982279, 'lng': 28.19409, '人数': 1 },
                    { 'lat': 113.280637, 'lng': 23.125178, '人数': 3 },
                    { 'lat': 110.33119, 'lng': 20.031971, '人数': 8 },
                    { 'lat': 1.065735, 'lng': 30.659462, '人数': 7 },
                    { 'lat': 8.948024, 'lng': 34.263161, '人数': 3 },
                    { 'lat': 3.823557, 'lng': 36.058039, '人数': 5 }
                ]
            }
        }
    }
}
</script>
