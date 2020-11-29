<template>
    <transition name="el-zoom-in-top">
        <div
            :id="id"
            :class="className"
            :index = "index"
            :style="{height:height,width:width} "
            style=""
        >
            <div style="height: 100%;width: 100%;padding: 0.7vh 0 0.2vh ;line-height: 1 ">
                <div style="height: 100%;width: 100%; border-bottom:1px solid #1C487A ; ">
                    <div
                        style="height: 20px ;text-align:center;display: inline-block;
                     width: 18px ;border:1px solid rgba(28, 72, 122, 1);"
                    >
            <span
                style="font-size:12px ;font-family: SourceHanSansCN-Bold;
                      position:relative;top: 1px;  color: #00E5FF ;overflow: hidden"
            >
              {{ index }}
            </span>
                    </div>
                    <div style="height: 100% ;display: inline-block;width: 43% ;">
            <span
                style="font-size:80% ;font-family: SourceHanSansCN-Bold;
          position:relative;top: 2px; left: 9%;  color:#fff"
            >
              {{ message }}
            </span>
                    </div>
                    <div style="height: 100% ;text-align: right;display: inline-block;width: 37% ;">
            <span
                style="font-size:80% ;font-family: SourceHanSansCN-Bold;
          position:relative;top: 2px; right: 0%;  color: #fff"
            >
              {{ time }}
            </span>
                    </div>

                </div>
            </div>
        </div>
    </transition>
</template>

<script>
export default {
    name: "messageNotice",
    props:{
        id:{
            type: String,
            require:true
        },
        message:{
            type: String,
            require: true
        },
        time:{
            type: String,
            require: true
        },
        height: {
            type: String,
            require: true
        },
        width: {
          type: String
        },
        index: {
            type: Number
        }
    },
    data(){
        return{
            className: ""
        }
    }
}
</script>

<style scoped>

</style>
