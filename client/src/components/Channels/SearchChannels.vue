<script lang="ts" setup>

import {
  Edit,
} from '@element-plus/icons-vue'
import {ref} from "vue";
import {useRoute} from "vue-router";

const input = ref('');

const route = useRoute()

</script>


<template>
  <div class="flex justify-between mb-2">
    <div class="">
      <el-input v-model="input" size="small" style="width: 140px" placeholder="Поиск канала" />
    </div>
    <router-link :to="{name: 'addChannel'}">
      <el-button type="primary" :icon="Edit"  size="small">
        Добавить канал
      </el-button>
    </router-link>
  </div>
</template>

<style scoped>

</style>
