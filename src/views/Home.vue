<template>
<div id="wrapper">  
            
			<header id="header">
			    <div class="container main-menu">
			    	<div class="row align-items-center justify-content-between d-flex">
				      <div id="logo">
				        <a href="#"><img :src="'./img/logo.png'" alt="" title="" /></a>
				      </div>
				      <nav id="nav-menu-container">
				        <ul class="nav-menu">			              
				        </ul>
				      </nav><!-- #nav-menu-container -->		    		
			    	</div>
			    </div>
			</header><!-- #header -->
			
			<!-- start banner Area -->
			<section class="banner-area relative" id="home">
				<div class="container">
					<div class="overlay overlay-bg"></div>
					<div class="row fullscreen d-flex align-items-center justify-content-start">
						<div class="banner-content col-lg-8 col-md-12">
							<h1 class="text-uppercase">
								Adopt Us. <br>
								We need your help.		
							</h1>
							<router-link to="/pets/1" class="primary-btn header-btn text-uppercase">View our pets!</router-link>
						</div>											
					</div>
				</div>
			</section>
			<!-- End banner Area -->

			<!-- Start image-carusel Area -->
			<section class="image-carusel-area">
				<div class="container">
					<div class="row">
						<div class="active-image-carusel">
							<div class="single-image-carusel">
								<img class="img-fluid" src="/img/c1.jpg" alt="">
							</div>
							<div class="single-image-carusel">
								<img class="img-fluid" src="/img/c2.jpg" alt="">
							</div>
							<div class="single-image-carusel">
								<img class="img-fluid" src="/img/c3.jpg" alt="">
							</div>
							<div class="single-image-carusel">
								<img class="img-fluid" src="/img/c4.jpg" alt="">
							</div>	
							<div class="single-image-carusel">
								<img class="img-fluid" src="/img/c1.jpg" alt="">
							</div>
							<div class="single-image-carusel">
								<img class="img-fluid" src="/img/c2.jpg" alt="">
							</div>
							<div class="single-image-carusel">
								<img class="img-fluid" src="/img/c3.jpg" alt="">
							</div>
							<div class="single-image-carusel">
								<img class="img-fluid" src="/img/c4.jpg" alt="">
							</div>
							<div class="single-image-carusel">
								<img class="img-fluid" src="/img/c1.jpg" alt="">
							</div>
							<div class="single-image-carusel">
								<img class="img-fluid" src="/img/c2.jpg" alt="">
							</div>
							<div class="single-image-carusel">
								<img class="img-fluid" src="/img/c3.jpg" alt="">
							</div>
							<div class="single-image-carusel">
								<img class="img-fluid" src="/img/c4.jpg" alt="">
							</div>															
						</div>
					</div>
				</div>	
			</section>
			<!-- End image-carusel Area -->




</div>

</template>

<script>

import { usePetsStore } from '@/store/pets'
import { usePetCategoriesStore } from '@/store/petcategories'

export default {

	setup() {
		const petsStore = usePetsStore()
		const petcategoriesStore = usePetCategoriesStore()		
		return { petsStore, petcategoriesStore }
  	},

    components: {
    },
   
    mounted() {
        this.petsStore.getPetsDB()
        this.petcategoriesStore.getCategoriesDB()
    },

}

</script>

<style scoped>
</style>