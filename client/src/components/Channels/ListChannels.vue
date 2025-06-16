<script lang="ts" setup>
import { onMounted, ref, computed } from 'vue'
import type { PaginationIntefaces } from "@/services/Interfaces/BaseIntefaces.ts"
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

const count = ref(10)
const loading = ref(false)
const disabled = computed(() => loading.value || noMore.value)
const noMore = computed(() => count.value >= 20)

const load = () => {
    loading.value = true
    setTimeout(() => {
        count.value += 2
        loading.value = false
    }, 2000)
}

</script>

<template>
    <ul v-infinite-scroll="load"
        class="list flex flex-col gap-2 pb-2 overflow-y-scroll h-5/6"
        :infinite-scroll-disabled="disabled">
        <ChannelCard v-for="channel in channels" :key="channel.oid" :channel=channel>
        </ChannelCard>
    </ul>
</template>

<style scoped>
.list{
  height: 92%;
}
</style>
