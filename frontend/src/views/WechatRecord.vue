<template>
  <el-container style="height: 100%; width: 100%;  flex-direction: column; ">
    <el-container class="topImage">
      <el-image style="width: 100%; height: 450px;" src="/purpleImg_title.jpg" />
    </el-container>
    <el-container style="flex-direction: row; justify-content: space-between">
      <el-container class="item">
        <el-text  class="item_title" >话痨们的口头禅是...</el-text>
      </el-container>
      <el-container class="item">
        <el-text  class="item_title">our mood</el-text>
      </el-container>
      <el-container class="item">
        <el-text  class="item_title" >喜欢说...给你听</el-text>
      </el-container>
    </el-container>
  </el-container>
</template>

<script setup>
</script>

<style scoped>
.topImage{
  align-items: center;
  width: 100%;
  height: 350px;
}
.item_title{
  font-size: 30px;
  font-family: "LXGW WenKai Mono Bold";
  font-weight: 8;
  color: rgba(23, 23, 24, 0.85);
  margin-top: 5px;
}
.item{
  flex-direction: column;
  justify-content: start;
  margin: 10px;
  border-radius: 15px;
  border-top: 2px solid rgba(23, 23, 24, 0.75);
  border-bottom: 2px solid rgba(23, 23, 24, 0.75);
  border-left: 1px solid rgba(23, 23, 24, 0.75);
  border-right: 1px solid rgba(23, 23, 24, 0.75);
}
</style>