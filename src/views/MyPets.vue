<template>
<div>


  
<Header />













<Footer />

</div>
</template>

<script>
import Footer from '@/components/Footer.vue'
import Header from '@/components/Header.vue'

import { useAdoptionsStore } from '@/store/adoptions'

export default {
	setup() {
		const adoptionsStore = useAdoptionsStore()	
		return { adoptionsStore }
  	}, 
    components: {
		Footer,
        Header
	},
	data() {
		return {
			adoptions: [],
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

<style scoped>
</style>