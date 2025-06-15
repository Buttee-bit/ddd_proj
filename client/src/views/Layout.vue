<template>
  <div class="flex flex-col h-screen">
    <Header class="h-10 flex-shrink-0"/>
    <div class="flex-1 overflow-y-auto bg-blue-100/70 flex flex-col items-center pt-2">
      <slot></slot>
    </div>
    <Footer class="flex-shrink-0"/>
  </div>
</template>

<script lang="ts" setup>
import Footer from '@/components/Footer/Footer.vue'
import Header from "@/components/Header/Header.vue";
</script>
