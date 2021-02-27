# tp_ros_Fadhul
## FONCTIONEMENT
Le programme fonctionne de la maniere suivante :
* Le fichier **src** qui contient le fichier **publisher.py** et le fichier lanch qui va nous permettre de lancer nos deux noeud:
   * **le publisher** qui publie les coordonnés de deux points (x,y) suivant sa trajectoir
   * Et le Bouton_gui qui se trouve à l'adresse git suivante https://github.com/Kramoth/button_gui 
 ce dernier nous permet d'actionner, d'arreter/faire marcher  notre sricpt **publisher.py**
 Tout ce processus peut etre suivit sur l'environnement graphique RVIZ .
## LANCEMENT DU SCRIPT
 
 Pour lancer script on utilise les commande suivantes :

 ```rosrun tp_ros_fadhul trajectoir.launch```

 Ensuite 

 ```rosrun tp_ros_fadhul publisher.py```