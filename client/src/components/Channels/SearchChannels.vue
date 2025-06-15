<script lang="ts" setup>

import {
  Edit,
} from '@element-plus/icons-vue'
import {ref} from "vue";

const input = ref('');


</script>


<template>
  <div class="flex justify-between ">
    <div class="">
      <el-input v-model="input" size="small" style="width: 140px" placeholder="Поиск канала" />
    </div>
    <el-button type="primary" :icon="Edit"  size="small">
      Добавить канал
    </el-button>
  </div>
  <br class="w-full">
</template>

<style scoped>

</style>
