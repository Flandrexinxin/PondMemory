<template>
  <el-row style="flex-direction: column; justify-content: start; align-items: center;width: 100%; height: 100%; margin-top: 140px;">
    <el-row style="flex-direction: column; justify-content: center; align-items: center;width: 90%; height: fit-content; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); border-radius: 10px; padding: 0 20px 50px 20px ">
      <el-avatar :size="120"  :src="UserInfo.avatar[0]" style="margin-top: -60px; box-shadow: 0 0px 5px 2px rgba(0, 0, 0, 0.19); margin-bottom: 30px"/>
      <el-row justify="center" align="middle">
        <span style="font-size: 35px; color: #313131; margin-bottom: 14px">{{UserInfo.userName}}</span>
<!--        <el-button size="small" round @click="" style="padding: 0 5px 0 5px"><el-icon><Edit /></el-icon></el-button>-->
      </el-row>
      <el-row justify="center" align="middle">
        <span style="font-size: 18px; color: #868686">{{UserInfo.signature}}</span>
<!--        <el-button size="small" round @click="" style="padding: 0 5px 0 5px"><el-icon><Edit /></el-icon></el-button>-->
      </el-row>

      <el-row>

      </el-row>
    </el-row>
  </el-row>
</template>

<script setup lang="ts">
import {getUserInfo} from "@/utils/auth.ts";
import {ref} from "vue";
import {Edit} from "@element-plus/icons-vue";

const UserInfo = ref(getUserInfo())
const form = ref({
  userName: '',
  signature: ''
})


const onClickEditUserNameBtn = () => {

}

const onClickEditSignatureBtn = () => {

}
</script>

<style scoped>

</style>
