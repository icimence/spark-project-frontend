<template>
	<div>
		<p>Home page</p>
		<p>Random number from backend: {{ randomNumber }}</p>
        <WordCloud></WordCloud>
        <BarChart></BarChart>
        <LineChart></LineChart>
        <RoseMap></RoseMap>
        <MyMap></MyMap>
	</div>
</template>

<script>
import axios from 'axios'
import WordCloud from "./WordCloud";
import LineChart from "./LineChart";
import RoseMap from "./RoseMap";
import BarChart from "./BarChart";
import MyMap from "./Map";
export default {
    components: {RoseMap, LineChart, BarChart, WordCloud,MyMap},
    data () {
		return {
			randomNumber: 0
		}
	},
	methods: {
		getRandomInt (min, max) {
			min = Math.ceil(min)
			max = Math.floor(max)
			return Math.floor(Math.random() * (max - min + 1)) + min
		},
		getRandom () {
			this.randomNumber = this.getRandomFromBackEnd()
		},
		getRandomFromBackEnd () {
			const path = `http://localhost:5000/api/random`
			axios.get(path)
				.then(response => {
					this.randomNumber = response.data.randomNumber
				})
				.catch(error => {
					console.log(error)
				})
		},
		times(){
			return setInterval(()=>{
				this.getRandomFromBackEnd()
			},100)
		}
	},
	destroyed(){
		clearInterval(this.times)
	},
	created () {
		this.getRandom()
	},
	mounted(){
		this.times()
	}
}
</script>
