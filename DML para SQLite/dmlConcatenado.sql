INSERT INTO comuna (id_comuna,descripcion_comuna) VALUES
	 (1,'Santiago'),
	 (2,'Cerrillos'),
	 (3,'Cerro Navia '),
	 (4,'Conchali'),
	 (5,'El Bosque'),
	 (6,'Estacion Central'),
	 (7,'Huechuraba'),
	 (8,'Independencia'),
	 (9,'La Cisterna'),
	 (10,'La Florida');
INSERT INTO comuna (id_comuna,descripcion_comuna) VALUES
	 (11,'La Granja'),
	 (12,'La Pintana'),
	 (13,'La Reina'),
	 (14,'Las Condes'),
	 (15,'Lo Barnechea'),
	 (16,'Lo Espejo'),
	 (17,'Lo Prado'),
	 (18,'Macul'),
	 (19,'Maipú'),
	 (20,'Ñuñoa');
INSERT INTO comuna (id_comuna,descripcion_comuna) VALUES
	 (21,'Pedro Aguirre Cerda'),
	 (22,'Peñalolen'),
	 (23,'Providencia'),
	 (24,'Pudahuel'),
	 (25,'Quilicura'),
	 (26,'Quinta Normal'),
	 (27,'Recoleta'),
	 (28,'Renca'),
	 (29,'San Joaquín'),
	 (30,'San Miguel');
INSERT INTO comuna (id_comuna,descripcion_comuna) VALUES
	 (31,'San Ramón'),
	 (32,'Vitacura'),
	 (33,'Puente Alto'),
	 (34,'Pirque'),
	 (35,'San José de Maipo'),
	 (36,'Colina'),
	 (37,'Lampa'),
	 (38,'Til Til'),
	 (39,'San Bernardo'),
	 (40,'Buin');
INSERT INTO comuna (id_comuna,descripcion_comuna) VALUES
	 (41,'Calera de Tango'),
	 (42,'Paine'),
	 (43,'Melipilla'),
	 (44,'Alhué'),
	 (45,'Curacaví'),
	 (46,'María Pinto'),
	 (47,'San Pedro'),
	 (48,'Talagante'),
	 (49,'El Monte'),
	 (50,'Isla de Maipo');
INSERT INTO comuna (id_comuna,descripcion_comuna) VALUES
	 (51,'Padre Hurtado'),
	 (52,'Peñaflor');

INSERT INTO estado_pedido (id_estado,descripcion_estado) VALUES
	 (1,'Pendiente'),
	 (2,'Entregado'),
	 (3,'Cancelado');

INSERT INTO preguntas_frecuentes (id_pregunta,pregunta,respuesta) VALUES
	 (1,'¿Tienen opciones veganas?','Por el momento no ofrecemos opciones veganas.'),
	 (2,'¿Que tipos de masas ofrecen?','Actualmente solo estamos ofreciendo masa a la piedra.'),
	 (3,'¿Tienen sucursales para ir a comer?','Actualmente no ofrecemos servicio de restaurante, solo delivery.');

INSERT INTO productos (id_producto,desc_corta,desc_larga,precio_real,precio_oferta,path_imagen,tipo_producto_seq_tipproduct) VALUES
	 (1,'Pizza Pepperoni','Mozzarella, Pepperoni',9990,7990,'Ppepper.jgp',1),
	 (2,'Pizza Napolitana','Mozarella, Tomate',9990,6990,'Pnapolitana.jpg',1),
	 (3,'Pizza Margarita','Mozarella, tomate cherry, albahaca',9990,7990,'Pmargarita.jpg',1),
	 (4,'Pollo BBQ','Salsa BBQ mix, mozarella, pollo, cebolla',13990,11990,'Pbbq.jpg',1),
	 (5,'Pizza al Pesto','Mozarella, tomate cherry, pesto',9990,9990,'Ppesto.jpg',1),
	 (6,'Pizza Hawaiiana','Piña, piña y más piña, jamón',15000,9890,'Phawaii.jpg',1),
	 (7,'Bebida 1.5','Bebidas 1.5Lt marca coca-cola & co, zero, light y normal.',10000,4990,'Abebida.jpg',2),
	 (8,'Masita','Masa de pizza con salsa de ajo, oregano y mozarrella',5990,3500,'Amasita.jpg',2),
	 (9,'Mayonesa Casera','100 GR de mayonesa Casera',1000,850,'NULL',3),
	 (10,'Salsa Marinara','Un cup de salsa marinara.',1000,750,'NULL',3);

INSERT INTO tipo_producto (seq_tipproduct,desc_tip_producto) VALUES
	 (1,'Pizza'),
	 (2,'Acompañamiento'),
	 (3,'Aderezo');

INSERT INTO auth_user (password,last_login,is_superuser,username,last_name,email,is_staff,is_active,date_joined,first_name) VALUES
	 ('pbkdf2_sha256$390000$0tz2jHPEbF44J0IzH10Ups$Z8g/VtawDYOP0/Pco/55r0O4w38nUrZRjpgOWq5Z3Fc=','2024-07-09 20:45:50.147650',1,'admin1','','vicerivera.a@gmail.com',1,1,'2024-07-09 20:45:14.871851',''),
	 ('pbkdf2_sha256$390000$dqFiQxvpDZji6onInnrSSe$57zOJDdE63IfrkJ+R74DSdfYNl2i4FgJ9OKZUMV2gOQ=',NULL,0,'albertAndres','Mansilla','churrasquito.psn@gmail.com',0,1,'2024-07-09 20:52:26','Albert'),
	 ('pbkdf2_sha256$390000$2YHrER9JJSGuWflMTB6w8k$sLZlUPZpFuFyBuBIxz5mhU9rgaOms50eFkaQ/QiRcJY=',NULL,0,'matiasF20','Flores','mat.floresm@duocuc.cl',0,1,'2024-07-10 01:39:18','Matias'),
	 ('pbkdf2_sha256$390000$idQQTVNmQQHC7szUwgbAXs$Owb8MC7uSz7AnHtULzAH5wBPWS5WYItgHDPyo0PvVrg=',NULL,1,'martNun3030','Nuñez','mart.nunezb@duocuc.cl',1,1,'2024-07-10 01:42:53','Martin'),
	 ('pbkdf2_sha256$390000$eNBSvPB3dHgOzLeS2TtRRM$DfFa8jZAV+qIwqCyKsk7R/ytQ07Rcl5H9VZsFd8iBxw=',NULL,0,'morris830','Morris','morris830@gmail.com',0,0,'2024-07-10 01:46:12','Ronald');



INSERT INTO usuario (telefono,direccion,comuna_id_comuna,user_id) VALUES
	 ('hihihi','Premio Nobel 5555',7,3),
	 ('gguggg','Manizales 1888',4,4),
	 ('9732379732','Av. Independencia 4599',4,5);



