
<template>
  <div class="bg-blue-300 flex items-center">
    <div class="h-4/5 ml-2 w-full flex justify-between">
      <div class="flex gap-3 items-center">
        <Logo></Logo>
        <p>ПО "НПО"</p>
      </div>
      <div class="flex gap-3 items-center mr-2">
        <div class="flex justify-center items-center bg-blue-100/70 rounded-full h-6 w-6 ">
          <el-icon><User /></el-icon>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup lang="ts">

import Logo from "@/components/Footer/Logo.vue";

</script>

<style scoped>

</style>
