<script lang="ts" setup>
import type {ChannelInterface} from "@/services/Channels/interface.ts";

const props = defineProps<{
  channel: ChannelInterface
}>();

</script>

<template>
  <p>
    {{ channel.oid }}
  </p>
</template>

<style scoped>

</style>
