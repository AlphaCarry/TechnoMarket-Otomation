veri>menucompenent
<script setup>

</script>

<template>
  <div class="magaza_menu">
    <div class="alt_menu">
      <router-link to="/magaza/ekle">Magaza Ekle</router-link>
      <a href="#">Magaza Liste</a>
    </div>
    <div class="icerik">
      <router-view></router-view>
    </div>
  </div>

</template>

<style scoped>
.magaza_menu{
  display:flex;
  border-radius: 5px;

}
.alt_menu{
  display: flex;
  flex-direction:column;
  padding-top: 20px;
  width: 20vw;
  border-radius: 5px;
}

.alt_menu a, .alt_menu a:visited {
  display: block;
  padding: 10px 20px;
  text-decoration: none;
  color: var(--menu-yazitipi-uzerinde);
  border-radius: 15px;
}
.alt_menu a:hover{
  background-color: var(--altbilgi-arkaplan);
  color: var(--menu-yazitipi-uzerinde)!important;
}

.icerik{
  width: 80vw;
}
.alt_menu a.router-link-active, .alt_menu a:visited.router-link-active{
  background-color: var(--altbilgi-arkaplan);
  color: var(--solicerik-yazitipi)!important;
}
</style>