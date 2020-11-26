<template>
	<div>
		<dv-full-screen-container>
			<dv-border-box-11 title="dv-border-box-11">dv-border-box-11</dv-border-box-11>
		</dv-full-screen-container>
	</div>
</template>

<script>
export default {
	data: [66,45],
	shape:'roundRect',
	name: "DataPresent",
	methods: {
		pieOutlineFunc() {
			var _this = this
			window.addEventListener('resize', function (e) {
				_this.$nextTick(() => {
					console.log(_this.$refs.pie2)
					_this.key++
				})
			})
		}
	},
	mounted() {
		this.pieOutlineFunc()
	}
}

</script>

<style scoped>
border_s{
	width: 50%;
	height: 100px;
}
</style>