import Vue from "vue"
import VueRouter from "vue-router"

Vue.use(VueRouter)

export const routes = [
    {
        path: "/test1",
        name: "test1",
        component: () => import("@/components/Page/Test1"),
        //keepAlive:true
    }
]

const router = new VueRouter({
    mode: "hash",
    scrollBehavior: () => ({ y: 0 }),
    routes,
})

export default router
