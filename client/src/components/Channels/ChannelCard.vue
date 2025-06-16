<script lang="ts" setup>
import type {ChannelInterface} from "@/services/Channels/interface.ts";
import {computed} from "vue";

const props = defineProps<{
  channel: ChannelInterface
}>();

const nameChannel = computed(()=> {
  return props.channel.url.slice(13).toUpperCase()
})

</script>

<template>
  <li class="flex w-full bg-blue-200 rounded-sm items-center pb-1 pt-1">
    <div class="flex w-14 justify-center">
      <div class="">
        <div class="flex bg-blue-50 rounded-full w-10 h-10">
        </div>
      </div>
    </div>
    <div class="flex flex-col w-4/5 ">
      <div class="flex justify-between" style="width: 100%">
        <p class="w-4/5 text-sm">{{ nameChannel }}</p>
        <a class="link flex items-center" :href=channel.url target="_blank">Ссылка
          <el-icon class="flex w-1/5">
            <Link :href="channel.url"/>
          </el-icon>
        </a>
      </div>
      <div class="flex flex-col">
        <p class="text-sm flex text-gray-500 gap-0.5 self-center">
          <p class="underline">Подписчиков:</p>
          <p class="">{{ channel.subscribers }}</p>
        </p>
        <div class="mt-1 mb-1 text-sm flex w-full justify-between">
          <button class="bg-blue-100 p-0.5 rounded-sm">Аналитика</button>
          <button class="bg-blue-100 p-0.5 rounded-sm">Подписаться</button>
        </div>
      </div>
    </div>


  </li>
</template>

<style scoped>
.el-divider--horizontal{
  margin-top: 3px;
  margin-bottom: 3px;
  border-top: 1px #5d71a9 var(--el-border-style);
}
.link{
  color: #0c91ef;
  text-decoration: underline #0c91ef;
}
</style>
