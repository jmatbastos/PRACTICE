<template>
	<header id="header">
	  <div class="container main-menu">
		  <div class="row align-items-center justify-content-between d-flex">
			<div id="logo">
			  <a href="#"><img src="/img/logo.png" alt="" title="" /></a>
			</div>
			<nav id="nav-menu-container">
			  <ul v-if="userIsEmpty" class="nav-menu">
				<li><router-link to="/pets/1">Dogs</router-link></li>
				<li><router-link to="/pets/2">Cats</router-link></li>
				<li><router-link to="/register">Register</router-link></li>   
				<li><router-link to="/login">Login</router-link></li>                                                 						  
			  </ul>
			  <ul v-else class="nav-menu">
				<li><router-link to="/pets/1">Dogs</router-link></li>
				<li><router-link to="/pets/2">Cats</router-link></li>
				<li><router-link to="#">Welcome {{userName}}</router-link></li>	                                                                         
				<li><router-link to="/mypets">My pets</router-link></li>
				<li><a @click.prevent="logout" href="/logout">Logout</a></li>					  
			  </ul>                        
			</nav><!-- #nav-menu-container -->		    		
		  </div>
	  </div>
	</header><!-- #header -->
</template>

<script>

import { useUserStore } from '@/store/user'

export default {

setup() {
const userStore = useUserStore()
return { userStore }
},

methods: {
logout() {
  this.userStore.logoutUser()
  localStorage.setItem('message', 'Bye, see you back soon!');
  this.$router.push('/message')
}
},
computed: {
userIsEmpty() {
  let obj = this.userStore.getUser
  return Object.keys(obj).length === 0;
},
userName() {
  return this.userStore.getUser.name
}
},

}


</script>
