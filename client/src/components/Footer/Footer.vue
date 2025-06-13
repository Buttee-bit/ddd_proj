<template>
  <div
    class='bg-blue-300 flex justify-center w-full h-12 '>
      <div class="flex w-full justify-between items-center">
        <div class="w-1/3">
          <BaseButton name='База Знаний' href="/liba"/>
        </div>
        <div class="w-1/3">
          <BaseButton name='Каналы' href="/channels"/>
        </div>
        <div class="w-1/3" >
          <BaseButton name='Новости' href="/news"  />
        </div>
      </div>
  </div>
</template>


<script lang="ts" setup>
import BaseButton from "@/components/Footer/Button/BaseButton.vue";
</script>
