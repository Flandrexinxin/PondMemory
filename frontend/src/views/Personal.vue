<template>
  <el-row style="flex-direction: column; justify-content: start; align-items: center;width: 100%; height: 100%; margin-top: 140px;">
    <el-row style="flex-direction: column; justify-content: center; align-items: center;width: 90%; height: fit-content; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); border-radius: 10px; padding: 0 20px 50px 20px ">
      <el-avatar @click="onClickAvatar" :size="120" style="margin-top: -60px; box-shadow: 0 0px 5px 2px rgba(0, 0, 0, 0.19); margin-bottom: 30px; border-radius: 50%;" :src="UserInfo.avatar[0] "/>
      <el-row justify="center" align="middle">
        <span style="font-size: 35px; color: #313131; margin-bottom: 14px">{{UserInfo.userName}}</span>
<!--        <el-button size="small" round @click="" style="padding: 0 5px 0 5px"><el-icon><Edit /></el-icon></el-button>-->
      </el-row>
      <el-row justify="center" align="middle">
        <span style="font-size: 18px; color: #868686">{{UserInfo.signature}}</span>
<!--        <el-button size="small" round @click="" style="padding: 0 5px 0 5px"><el-icon><Edit /></el-icon></el-button>-->
      </el-row>

      <el-row style="width: 100%; height: fit-content; margin: 40px 0 0 0 ">
        <el-descriptions
          title="个人信息"
          border
          style="width: 100%"
          :column="2"
        >
          <template #extra>
            <el-button v-if="!isUpdatingProfile" size="small" @click="onClickEditProfileBtn">修改信息</el-button>
            <el-row v-else>
              <el-button size="small" type="success" @click="onClickCommitChangeProfileBtn">确认</el-button>
              <el-button size="small" type="danger" @click="onClickCancelChangeProfileBtn">取消</el-button>
            </el-row>
          </template>

          <el-descriptions-item>
            <template #label>
              <el-row justify="start" align="middle">
                <el-image class="descriptions_icon" src="/icons/9165463_qr_code_icon.png"/>
                <el-row justify="center" align="middle" style="width: calc(100% - 26px)">
                  <span class="descriptions_label">用户ID</span>
                </el-row>
              </el-row>
            </template>
            <el-text>{{UserInfo.userId}}</el-text>
          </el-descriptions-item>

          <el-descriptions-item>
            <template #label>
              <el-row justify="start" align="middle">
                <el-image class="descriptions_icon" :src="UserInfo.sex == 'male' ? '/icons/9165726_user_male_avatar_icon.png' : '/icons/9165712_user_female_avatar_icon.png'"/>
                <el-row justify="center" align="middle" style="width: calc(100% - 26px)">
                  <span class="descriptions_label">用户名</span>
                </el-row>
              </el-row>
            </template>
            <el-input v-if="isUpdatingProfile" v-model="form.userName" placeholder="请输入用户名"/>
            <el-text v-else>{{UserInfo.userName}}</el-text>
          </el-descriptions-item>

          <el-descriptions-item>
            <template #label>
              <el-row justify="start" align="middle">
                <el-image class="descriptions_icon" :src="UserInfo.sex == 'male' ? '/icons/9165411_male_gender_icon.png' : '/icons/9165554_femaile_gender_icon.png' "/>
                <el-row justify="center" align="middle" style="width: calc(100% - 26px)">
                  <span class="descriptions_label">性别</span>
                </el-row>
              </el-row>
            </template>
            <el-switch
                v-if="isUpdatingProfile"
              v-model="form.sex"
              inline-prompt
              style="--el-switch-on-color: #1a90e5; --el-switch-off-color: #d27373"
              active-text="男"
              inactive-text="女"
            />
            <el-text v-else>{{UserInfo.sex == 'male' ? '男' : '女'}}</el-text>
          </el-descriptions-item>

          <el-descriptions-item>
            <template #label>
              <el-row justify="start" align="middle">
                <el-image class="descriptions_icon" src="/icons/9165561_mail_email_icon.png"/>
                <el-row justify="center" align="middle" style="width: calc(100% - 26px)">
                  <span class="descriptions_label">邮箱</span>
                </el-row>
              </el-row>
            </template>
            {{UserInfo.email}}
          </el-descriptions-item>

          <el-descriptions-item>
            <template #label>
              <el-row justify="start" align="middle">
                <el-image class="descriptions_icon" src="/icons/9165610_right_align_icon.png"/>
                <el-row justify="center" align="middle" style="width: calc(100% - 26px)">
                  <span class="descriptions_label">个性签名</span>
                </el-row>
              </el-row>
            </template>
            <el-input type="textarea" v-model="form.signature" v-if="isUpdatingProfile" placeholder="请输入个性签名"/>
            <el-text v-else>{{UserInfo.signature}}</el-text>
          </el-descriptions-item>
        </el-descriptions>
      </el-row>
    </el-row>
  </el-row>

  <el-dialog
    v-model="updateAvatarDialogShow"
    width="90%"
    style="max-width: 800px;"
  >
    <template #header="{close, titleId, titleClass}">
      <el-row justify="center" align="middle" style="width: 100%">
        <span :id="titleId" :class="titleClass" style="font-size: 24px; color: #383838">修改头像</span>
      </el-row>
    </template>
    <el-row justify="center" align="middle" style="height: 100%; width: 100%">
      <el-tabs v-model="tabActivateName" style="width: 100%">
        <el-tab-pane label="插图" name="first">插图</el-tab-pane>
        <el-tab-pane label="上传" name="second">上传</el-tab-pane>
      </el-tabs>
    </el-row>
  </el-dialog>

</template>

<script setup lang="ts">
import {getUserInfo, setUserInfo} from "@/utils/auth.js";
import {ref} from "vue";
import { changeUserProfile, userProfile } from '@/api/user.js'
import {ElMessage} from "element-plus";

const tabActivateName = ref("first")
const updateAvatarDialogShow = ref(false)
const UserInfo = ref(getUserInfo())
const form = ref({
  userName: '',
  signature: '',
  sex: true
})

const isUpdatingProfile = ref(false)

const onClickEditUserNameBtn = () => {

}

const onClickEditSignatureBtn = () => {

}

const resetForm = () => {
  form.value.userName = UserInfo.value.userName
  form.value.signature = UserInfo.value.signature
  form.value.sex = UserInfo.value.sex == 'male' ? true : false
}

const onClickEditProfileBtn = () => {
  resetForm()
  isUpdatingProfile.value = true
}

const onClickCancelChangeProfileBtn = () => {
  resetForm()
  isUpdatingProfile.value = false
}

const onClickCommitChangeProfileBtn = () => {
  changeUserProfile(form.value)
      .then((res) => {
        getNewUserProfile().then(() => {
          UserInfo.value = getUserInfo()
          resetForm()
          ElMessage({
            type: 'success',
            message: "修改成功！"
          })
          isUpdatingProfile.value = false
        })
      })
}

const getNewUserProfile = () => {
  return userProfile().then((res) => {
    let userInfo = res.data.userInfo;
    setUserInfo(userInfo);
  })
}

const onClickAvatar = () => {
  updateAvatarDialogShow.value = true
}

</script>

<style scoped>
.descriptions_label{
  font-weight: bold;
  margin: 0 0 0 8px;
}

.descriptions_icon{
  width: 18px;
  height: 18px;
}

.top_avatar_editor_layer:hover{
  background: rgb(0,0,0,0.9);
  position: relative;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  width: 120px;
  height: 120px;
  border-radius: 50%;
  z-index: 100;
}

</style>
