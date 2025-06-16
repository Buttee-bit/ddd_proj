<script setup lang="ts">

import {ref} from "vue";
import {addChannel} from "@/services/Channels/channels.api.ts";

let user_input = ref('')

async function addChannelButton(user_input:string){
  await addChannel(user_input).then(([error, response]) =>{
    console.log('[error, response]', [error, response])
    if (error){
      console.error(error)
    }
  })
}

</script>

<template>
  <div class="flex justify-between w-11/12 gap-3">
    <el-input  v-model="user_input" class="w-2/3" size="small" placeholder="url канала">

    </el-input>

    <el-button class="w-1/3" size="small" @click="addChannelButton(user_input)">
      Добавить канал
    </el-button>
  </div>
</template>

<style scoped>

</style>
