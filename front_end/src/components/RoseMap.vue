<template>
    <ve-ring :data="chartData"  jude-width=true height="100%" :settings="chartSettings"></ve-ring>
</template>

<script>
import axios from 'axios'
export default {
    name:'RoseMap',
    data () {
        this.chartSettings = {
            roseType: 'radius'
        }
        return {
            chartData: {
                columns: ['state', 'number'],
                rows: []
            }
        }
    },
    methods:{
        getRoseMapRowsFromBackend(){

            const path= `http://localhost:5000/api/answer`
            axios.get(path)
                .then(response => {
                    console.log(response.data)
                    this.chartData.rows = response.data
                })
                .catch(error =>{
                    console.log(error)
                })
        },
        times(){
            return setInterval(()=>{
                this.getRowsFromBackend()
            },2000)
        }
    },
    destroyed() {
        clearInterval(this.times())
    },
    mounted() {
        this.times()
    },
    created() {
        this.getRoseMapRowsFromBackend()
    }
}
</script>
