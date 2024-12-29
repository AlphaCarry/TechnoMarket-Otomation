import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";

export const magazaDukkaniKullan = defineStore('magaza', () => {
    const seciliMagaza = ref({
        id: 0,
        olusturulma_tarihi: '',
        guncelleme_tarihi: '',
        magaza_adi: '',
        magaza_adresi: '',
        magaza_telefon: '',
        magaza_yetkili_kisi: ''
    });
    const yeniMagaza = ref({
        magaza_adi: '',
        magaza_adres: '',
        magaza_telefon: '',
        magaza_yetkili_kisi: '',
    });
    const magazalar = ref([]);

    const api = axios.create({
        baseURL: 'http://127.0.0.1:5000/api/v1'
    });

    async function tumMagazalariGetir() {
        try {
            const response = await api.get('/magaza');
            magazalar.value = response.data;
        } catch (error) {
            console.error("Mağazalar getirilirken hata oluştu:", error);
        }
    }


    async function ekle(fonksiyon) {
        console.log("Ekleniyor...");
        try {
            const response = await api.post('/magaza', yeniMagaza.value);
            if (fonksiyon) {
                fonksiyon(response.data);
            } else {
                console.log(response.data);
            }
            yeniMagaza.value = {
                magaza_adi: '',
                magaza_adres: '',
                magaza_telefon: '',
                magaza_yetkili_kisi: '',
            };
            await tumMagazalariGetir();
            return response.data;
        } catch (error) {
            console.error("Ekleme sırasında hata oluştu:", error);
            return null;
        }
    }

    async function guncelle(magaza) {
        console.log("Güncelleniyor...", magaza);
        try {
            const response = await api.put(`/magaza/${magaza.id}`, magaza);
            console.log("Güncelleme başarılı:", response.data);
            await tumMagazalariGetir();
            return response.data;
        } catch (error) {
            console.error("Güncelleme sırasında hata oluştu:", error);
            return null;
        }
    }

    async function sil(id) {
        console.log("Siliniyor...", id);
        try {
            const response = await api.delete(`/magaza/${id}`);
            console.log("Silme başarılı:", response.data);
            await tumMagazalariGetir();
            return true;
        } catch (error) {
            console.error("Silme sırasında hata oluştu:", error);
            return false;
        }
    }

    async function ara(terim) {
        console.log("Aranıyor...", terim);
        try {
            const response = await api.get(`/magaza?q=${terim}`);
            magazalar.value = response.data;
        } catch (error) {
            console.error("Arama sırasında hata oluştu:", error);
        }
    }

    return { seciliMagaza, yeniMagaza, magazalar, ekle, sil, guncelle, ara, tumMagazalariGetir };
});