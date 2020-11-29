<template>
    <div >
        <messageNotice
            v-for="(item,key) in noticeManage"
            v-if = "item.index in displayIndex"
            width="100%"
            height="20%"
            :key="key"
            :index="item.index"
            :message="item.message"
            :time="item.time"
        />
    </div>
</template>

<script>

export default {

    name: "Element",
    data() {
        return {
            displayIndex :[1,2,3,4,5,6,7,8],
            startIndex:1,
            endIndex:6,
            noticeManage: [
                {index: 1, message: '会议通知', time: '2019-11-27'},
                {index: 2, message: '电梯故障通知', time: '2019-11-27'},
                {index: 3, message: '停车通知', time: '2019-11-27'},
                {index: 4, message: '停水通知', time: '2019-11-27'},
                {index: 5, message: '社区互动', time: '2019-11-27'},
                {index: 6, message: '会议通知', time: '2019-11-27'},
                {index: 7, message: '电梯故障通知', time: '2019-11-27'},
                {index: 8, message: '停车通知', time: '2019-11-27'},
                {index: 9, message: '停气通知', time: '2019-11-27'},
                {index: 10, message: '社区互动', time: '2019-11-27'}
            ],
        }
    },
    created() {
        setInterval(() => {
            if (this.displayIndex[this.displayIndex.length - 1] < this.noticeManage.length){
                this.displayIndex = this.displayIndex.splice(0,1)
            }
            // if (this.noticeManage.length - this.startIndex < 3) {
            //     console.log("即将用尽数据")
            //     this.startIndex = 0
            //     this.endIndex = 8
            // } else {
            //     console.log("数据开始轮播")
            //     this.startIndex++
            //     setTimeout(() => { this.endIndex++ }, 10)
            // }
        }, 2000)
    }
}
</script>

<style scoped>

</style>
