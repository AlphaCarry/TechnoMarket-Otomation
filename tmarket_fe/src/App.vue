<script setup>


import BaslikBileseni from "@/bilesenler/baslikbileseni.vue";
import MenuBileseni from "@/bilesenler/menubileseni.vue";
import IcerikBileseni from "@/bilesenler/icerikbileseni.vue";
import AltBilgiBileseni from "@/bilesenler/altbilgibileseni.vue";
import {storeToRefs} from "pinia";
import Tema_secici from "@/bilesenler/ortak/tema_secici.vue";

import {temaDukkaniKullan} from "@/dukkan/TemaDukkani.js";

const tema_dukkani = temaDukkaniKullan();

const {secili_tema} = storeToRefs(tema_dukkani);



</script>

<template>
  <div class="kapsayici" :class="secili_tema">
    <BaslikBileseni/>
    <MenuBileseni/>
    <IcerikBileseni/>
    <AltBilgiBileseni/>
    <Tema_secici/>

  </div>
</template>

<style scoped>

.kapsayici {
  display: flex;
  flex-direction: column;
}

</style>