import MagazaMenuComponent from "@/bilesenler/veri/magazamenucomp.vue";
import {createRouter, createWebHashHistory} from "vue-router";
import BosMenu from "@/bilesenler/ortak/BosMenu.vue";
import MagazaEklemeComponent from "@/bilesenler/veri/magazaeklemecomp.vue";

export const router = createRouter({
    history:createWebHashHistory(),
    routes:[
        {path:'/',component: BosMenu},
        {
            path:'/magaza',component: MagazaMenuComponent,
            children:[{

                path:'Ekle',
                component: MagazaEklemeComponent
            }]
        },
    ]
})