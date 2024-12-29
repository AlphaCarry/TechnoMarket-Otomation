<script setup>
import {storeToRefs} from "pinia";
import {temaDukkaniKullan} from "@/dukkan/TemaDukkani.js";
const tema_dukkani = temaDukkaniKullan();

const {secili_tema} = storeToRefs(tema_dukkani);

</script>

<template>
  <div class="alt_bilgi">
    Secili Tema {{ secili_tema }}
  </div>

</template>

<style scoped>

.alt_bilgi{
  flex-grow: 2;
  background-color:var(--altbilgi-arkaplan);
  color: var(--altbilgi-yazitipi);
  border-radius: 5px;
}

</style>