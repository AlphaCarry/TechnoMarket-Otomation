import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const temaDukkaniKullan = defineStore('tema', () => {
    const secili_tema = ref("acik");

    // Tema listesi (isteğe bağlı)
    const temalar = ref([
        { ad: "acik", sinif: "light-theme" },
        { ad: "koyu", sinif: "dark-theme" },
        { ad: "mavi", sinif: "blue-theme" } // Örnek tema
    ]);

    // Seçili temanın sınıfını döndüren computed property
    const seciliTemaSinifi = computed(() => {
        const tema = temalar.value.find(t => t.ad === secili_tema.value);
        return tema ? tema.sinif : "light-theme"; // Varsayılan olarak açık tema sınıfı
    });

    // Temayı değiştiren fonksiyon
    function temayiDegistir(yeniTema) {
        if (temalar.value.some(t => t.ad === yeniTema)) { // Geçerli bir tema mı kontrolü
            secili_tema.value = yeniTema;
            localStorage.setItem('tema', yeniTema); // Temayı localStorage'e kaydet
        } else {
            console.error("Geçersiz tema:", yeniTema);
        }

    }

    // localStorage'dan temayı yükleyen fonksiyon (mağaza ilk oluşturulduğunda çalıştırılabilir)
    function temayiYukle() {
        const kaydedilmisTema = localStorage.getItem('tema');
        if (kaydedilmisTema && temalar.value.some(t => t.ad === kaydedilmisTema)) {
            secili_tema.value = kaydedilmisTema;
        }
    }

    temayiYukle(); // Mağaza oluşturulurken temayı yükle

    return { secili_tema, temalar, seciliTemaSinifi, temayiDegistir };
});