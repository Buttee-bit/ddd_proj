<script lang="ts" setup>
import {Collection, Memo, Paperclip} from '@element-plus/icons-vue'
import {computed} from 'vue'
import { useRoute } from 'vue-router'

const props = defineProps({
  name: String,
  href: String,
  is_active: Boolean,
})

const route = useRoute()

function getIcon(name: string) {
  if (name === 'Новости') {
    return Paperclip
  }
  if (name === 'База Знаний') {
    return Collection
  }
  if (name === 'Каналы') {
    return Memo
  }
  return null
}

const isActive = computed(() => {
  return route.path.includes(props.href)
})
</script>

<template>
  <router-link :to="{path: href}">
    <div :class="{'active': isActive, 'inactive': !isActive}">
      <div class="flex flex-col items-center">
        <el-icon>
          <component :is="getIcon(props.name)"/>
        </el-icon>
        <p class="text-sm font-extralight h-fit">{{ props.name }}</p>
      </div>
    </div>
  </router-link>
</template>

<style scoped>

.active {
  color: #f5e9e9;
  font-weight: bold;
}
</style>
