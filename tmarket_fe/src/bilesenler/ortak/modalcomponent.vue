<script setup>

import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {computed} from "vue";

const props =defineProps(['acik','kapanmaSebebi']);
const emits= defineEmits(['update:acik','update:kapanmaSebebi']);

const acikProp= computed({
  get(){
    return props.acik;
  },
  set(value){
    emits('update:acik',value);
  }
});
const kapanmaSebebiProp= computed({
  get(){
    return props.kapanmaSebebi;
  },
  set(value){
    emits('update:kapanmaSebebi',value);
  }
});

</script>

<template>
  <teleport to="body" v-if="acikProp" >
    <div class="soru arkaplan" @click="kapanmaSebebiProp='arkaplan';">
      <div class="soru tasiyici">
      </div>
      <div class="soru pencere">
        <div class="soru baslik">
          <div class="soru metin">
            <slot name="baslik">Onay</slot>
          </div>
          <div class="soru metin kapat" @click="kapanmaSebebiProp='carpi';">X</div>
        </div>
        <div class="soru icerik">
          <div class="soru simge"><font-awesome-icon :icon="['fas', 'circle-exclamation']" /></div>
          <div class="sorumetni">
            <slot name="sorumetni">Soru</slot>
          </div>
        </div>
        <div class="soru butonlar">
          <slot name="butonlar">
            <div class="soru buton olumlu">Evet</div>
            <div class="soru buton olumsuz">Hayır</div>
          </slot>
        </div>
      </div>
    </div>
  </teleport>
</template>

<style scoped>
div.soru.baslik{
  width: 30vw;
  display: flex;
  padding: 5px;
  font-size: 15pt;
  font-weight:bold ;
  justify-content: space-between;

}
div.soru.icerik{
  display: flex;
  padding: 5px;
  gap:5px;
}
div.soru.baslik .metin{
  font-size: 15pt;
  font-weight:bold ;
}
div.soru.butonlar{
  display: flex;
  padding: 5px;
  justify-content: space-between;
}
div.soru.butonlar div{
  padding: 10px 10px;
  cursor: pointer;
}
div.soru.metin.kapat{
  cursor: pointer;

}
div.soru.simge{
  color: #2e86c1;
  height: 50px;
  width: 50px;
}
div.soru.simge svg{
  width:100%;
  height: 100%;

}

div.sorumetni{
  max-width: 20vw;
}
div.soru.pencere{
  display: flex;
  background-color: #dfe1e9;
  border-radius: 8px;
  border: thin solid#34495e ;
  flex-direction:column ;
  font-family: 'Cuprum', sans-serif  ;
  z-index: 2;

}
div.soru.arkaplan{
  background-color: rgba(0,0,0,0.6);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  display: flex;
  justify-content:center;
  align-items: center;
}

div.soru.tasiyici{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
}
div.soru.buton.olumlu{
  background-color:springgreen;
  color: #1b2631;
}
div.soru.buton.olumlu:hover{
  background-color:mediumseagreen;
  color: #1b2631;
}

div.soru.buton.olumsuz{
  background-color:  #c0392b ;
  color: #1b2631;
}
div.soru.buton{
  border-radius: 5px;
}



</style>