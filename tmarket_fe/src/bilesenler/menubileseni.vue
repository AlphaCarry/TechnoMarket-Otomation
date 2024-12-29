<script setup>

</script>

<template>
  <div class="Menu">
    <router-link to="/magaza">Magaza</router-link>
    <router-link to="/magaza_bilgileri">Magaza Bilgileri</router-link>
    <router-link to="/urun_kategorisi">Ürün Kategorisi</router-link>
    <router-link to="/urun_ozellikleri">Ürün Özellikleri</router-link>
    <router-link to="/urun_yorumu">Ürün Yorumu</router-link>
    <router-link to="/musteri_yorumu">Musteri Yorumu</router-link>

    <router-link to="/siparis">Sipariş</router-link>

    <router-link to="/siparis_urunu">Sipariş Ürünü</router-link>
  </div>
</template>

<style >
.Menu{
  overflow: hidden;
  background-color: var(--menu-arkaplan);
  color: var(--menu-yazitipi);
  display: flex;
  border-radius: 5px;
}

.Menu a{
  color: var(--menu-yazitipi);
  text-align: center;
  padding: 14px 20px;
  text-decoration: none;
}

.Menu a:hover{
  background-color: var(--menu-arkaplan-uzerinde);
  color: var(--menu-yazitipi-uzerinde);
}

.Menu a.router-link-active{
  background-color: var(--menu-arkaplan-uzerinde);
  color: var(--menu-yazitipi-uzerinde);

}

</style>