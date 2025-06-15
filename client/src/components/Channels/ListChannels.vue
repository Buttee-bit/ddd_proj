<script lang="ts" setup>
import { onMounted, ref, Ref } from 'vue'
import { PaginationIntefaces } from "@/services/Interfaces/BaseIntefaces.ts"
import { getChannels } from "@/services/Channels/channels.api.ts"
import ChannelCard from "@/components/Channels/ChannelCard.vue";
import type { ChannelInterface } from "@/services/Channels/interface.ts"

const user_data = ref({
  pagination: {
    limit: 20,
    offset: 0,
    count: 0
  } as PaginationIntefaces
})

const channels:Ref<ChannelInterface[]> = ref<ChannelInterface[]>([])

onMounted(() => {
  getChannels(user_data.value.pagination).then(([error, response]) => {
    channels.value = response.data
    user_data.value.pagination = response.pagination
    if (error){
      console.log(error)
    }
  })
})
</script>

<template>
  <h2>Список каналов</h2>
  <ChannelCard v-for="channel in channels" :key="channel.id" :channel=channel>

  </ChannelCard>
</template>

<style scoped>
</style>
