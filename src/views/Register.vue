<template>
    <div>
   
        <Header />



            
                    



                        





        <Footer />

    </div>
</template>
<script>
import Footer from '@/components/Footer.vue'
import Header from '@/components/Header.vue'

import { useUserStore } from '@/store/user'

export default {
    name: 'register',
    setup() {
		const userStore = useUserStore()		
		return { userStore }
  	},     
    components: {
        Footer,
        Header
    },

    data() {
        return {
            name: '',
            email: '',
            password: '',
            passwordConfirm: '',        
        }
    },

    mounted() {
    },
    methods: {    
        
    },
    computed: {
               
    },

}
</script>