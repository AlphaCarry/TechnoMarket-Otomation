<script setup>

import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {ref} from "vue";
import {magazaDukkaniKullan} from "@/dukkan/magazadukkani.js";
import {storeToRefs} from "pinia";
import ModalComponent from "@/bilesenler/ortak/modalcomponent.vue";

const magazaDukkan =magazaDukkaniKullan();

const {yeniMagaza}= storeToRefs(magazaDukkan);

const  {ekle} = magazaDukkan;

const dialog_acik= ref(false);
function  magaza_bilgilerini_yazdir(){
  dialog_acik.value=true;
}

function form_resetle() { // Yeni fonksiyon: Formu sıfırlar
  magaza_adi.value = '';
  magaza_adresi.value = '';
  console.log("Form temizlendi fonksiyonu çalıştı!"); // Konsol kontrolü için
}

</script>

<template>
  <div class="data-form">
    <div class="satir">
      <div class="etiket">Magaza Adi</div>
      <div class="bilesen">
        <font-awesome-icon icon="cart-shopping"/>
        <input class="girdi" type="text" name="magaza_adi" v-model="yeniMagaza.magaza_adi">
      </div>
    </div>
    <div class="satir">
      <div class="etiket">Magaza Adresi</div>
      <div class="bilesen">
        <font-awesome-icon :icon="['fas', 'map-location-dot']"/>
        <textarea class="girdi" type="text" name="magaza_adresi" v-model="yeniMagaza.magaza_adres">
      </textarea>
      </div>
    </div>
    <div class="satir">
      <div class="etiket">Magaza Telefonu</div>
      <div class="bilesen">
        <font-awesome-icon :icon="['fas', 'phone']" />
        <input  class="girdi" name="magaza_telefonu" placeholder="0 (5XX) XXX XX XX" v-model="yeniMagaza.magaza_telefon">
      </div>
    </div>
    <div class="satir">
      <div class="etiket">Magaza Yetkili Kişisi</div>
      <div class="bilesen">
        <font-awesome-icon :icon="['fas', 'user-tie']" />
        <input class="girdi" type="text" name="magaza_yetkiili_kisi" v-model="yeniMagaza.magaza_yetkili_kisi">
      </div>
    </div>
    <div class="satir">
      <div class="butoncubugu">
        <div class="button olumlu" @click="magaza_bilgilerini_yazdir">Ekle</div>
        <div class="button olumsuz" @click="form_resetle">İptal</div> <!— Değiştirildi —>
      </div>
    </div>
  </div>
  <ModalComponent v-model:acik="dialog_acik" @update:kapanmaSebebi="sebep => {
    if(sebep==='carpi'){
      dialog_acik=false;
    }
  }">
    <template #baslik>
      Kaydetme Onayı
    </template>
    <template #sorumetni>
      Degisikleri kaydetmek isterdeginize emin misiniz?<br/>
      <span class="uyari"> Bu islem geri alınamaz.</span>
    </template>
    <template #butonlar>
      <div class="soru button olumlu" @click="ekle(()=>{dialog_acik=false;})">Evet</div>
      <div class="soru button olumsuz" @click="dialog_acik = false">Hayır</div>
    </template>
  </ModalComponent>
</template>

<style scoped>

span.uyari {
  font-size:8pt;
  color: orangered;
}
div.butoncubugu{
  display: flex;
  gap: 5px;
}

div.button{
  display: block;
  padding: 10px 10px;
  border-radius: 5px;
  cursor:pointer;
}
div.button.olumlu{
  background-color:springgreen;
  color: #1b2631;
}
div.button.olumlu:hover{
  background-color:mediumseagreen;
  color: #1b2631;
}

div.button.olumsuz{
  background-color:  #c0392b ;
  color: #1b2631;
}

.satir{
  display: flex;
  flex-direction: column;
  padding: 10px 150px;
}
.bilesen{
  display: flex;
  width: 100%;
  margin-bottom: 15px;
}

.bilesen > textarea{
  height: 150px;
}
.bilesen svg {
  padding: 10px;
  background: var(--menu-arkaplan);
  color: var(--menu-yazitipi);
  min-width: 50px;
  text-align: center;

}
.girdi {
  width: 100%;
  padding: 10px;
  outline: none;
  border: none;
}
.bilesen > .girdi:focus {
  border: 2px solid var(--menu-arkaplan);
}

</style>