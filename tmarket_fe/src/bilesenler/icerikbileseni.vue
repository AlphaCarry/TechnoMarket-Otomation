<script setup>

import SolIcerik from "@/bilesenler/alt_bilesenler/soicerik.vue";
import SagIcerik from "@/bilesenler/alt_bilesenler/saicerik.vue";
</script>

<template>
  <div class="icerik">
    <router-view>

    </router-view>
  </div>
</template>

<style scoped>
.icerik{
  display: flex;
  flex-direction: row;
  flex-grow: 20;

}

</style>