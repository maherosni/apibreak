CREATE DATABASE desayunos CHARACTER SET utf8mb4;

USE desayunos;

CREATE TABLE categorias(
    idcat INT PRIMARY KEY AUTO_INCREMENT,
    nomcat VARCHAR(50) NOT NULL
);

INSERT INTO categorias (nomcat) VALUES ('Clásico');
INSERT INTO categorias (nomcat) VALUES ('Típico');
INSERT INTO categorias (nomcat) VALUES ('De la Casa');
INSERT INTO categorias (nomcat) VALUES ('Gourmet');
INSERT INTO categorias (nomcat) VALUES ('Vegano');
INSERT INTO categorias (nomcat) VALUES ('Saludable');
INSERT INTO categorias (nomcat) VALUES ('Infantil');
INSERT INTO categorias (nomcat) VALUES ('Bebidas');
INSERT INTO categorias (nomcat) VALUES ('Adicionales');

CREATE TABLE productos(
    idprod INT PRIMARY KEY AUTO_INCREMENT,
    nomprod VARCHAR(50) NOT NULL,
    descriprod TEXT,
    precio DECIMAL(10,2) NOT NULL,
    idcat INT,
    CONSTRAINT fk_categorias FOREIGN KEY (idcat) REFERENCES categorias (idcat)
);

INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Huevos al gusto', 'Huevos revueltos o fritos freidos en mantequilla', 25000, 1);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Croasaint', 'Pieza de pan en forma de cuarto creciente lunar', 11000, 1);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Buñuelo', 'Preparada con harina de maíz y queso costeño, frito en aceite vegetal, en presentación de 70 gramos', 4000, 1);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Pan de Yuca', 'Preparado con almidón de yuca y queso de 50 gramos', 5000, 1);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Empanada de Trigo', 'Preparada con harina de trigo, rellena de arroz, carne molida y cilantro picado, frita en aceite vegetal', 5600, 1);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Empanada de Yuca', 'Preparada con yuca, rellena de arroz, huevo y cilantro picados, frita en aceite vegetal', 5000, 1);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Caldo al gusto', 'Preparado con papa negra y amarilla, tostado, sal y cilantro picado', 10000, 2);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Tamal al gusto', 'Masa de maíz envuelta en hojas de plátano, con verduras o garbanzos, cocido al vapor', 15000, 2);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Ayaco al gusto', 'Masa de maíz envuelta en hojas de mazorcas, con arroz, verduras y sal', 12000, 2);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Arepa santandereana', 'Arepa de maíz amarillo, molido con chicharrón, con grasa de cerdo y sal', '8000', 2);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Calentado', 'Plato de arroz, con papa, tajadas de maduro y cebolla junca picados', 25000, 3);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Carne Oreada', 'Porción de carne adobada y oreada, asada a la parrilla, acompañada de yuca, arepa santandereana y ensalada de tomate, cebolla, lechuga crespa, sal y limón', 35000, 3);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Papas Chorreadas', 'Plato de papas enchaquetadas cocidads, acompañadas de sofrito de cebolla junca, tomate, sal y aceite vegetal', 20000, 3);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Colada Dulce', 'Bebida caliente preparada con leche, maizena, vainilla, azúcar y canela', 15000, 3);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Tostadas Braunch', 'Tostadas integrales con guacamole, tomate cherry y queso ricota', 25000, 4);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Crepé de pollo', 'Crepé preparado con harina de linaza, yogur griego, pollo desmechado y sal marina', 20000, 4);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Quibbe Veggie', 'Quibbe vegano artesanal a base de lenteja, quinoa y sal marina', 15000, 5);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Sandwich de  tofu', 'Tofu previamente marinado, pan tajado, mortadela vegana, espinaca, tomate y queso vegetal', 16000, 5);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Cazuela de papa y vegetales', 'Papas salteadas en aceite de oliva, con cebolla roja, brócoli, kale y champiñones', 20000, 5);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Hotcakes de avena', 'Tres hotcakes preparados con una mezcla de avena y banano, agua, esencia y canela en polvo', 25000, 6);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Ensalada de Frutas al gusto', 'Fruta picada con hojuelas de avena o cornflakes, y yogur griego', 25000, 6);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Panqueques', 'Tortas elaboradas a partir de una mezcla de avena, estevia, sal, leche, miel y chocolate', 15000, 7);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Kellogs', 'Hojuelas azucaradas o achocolatadas en leche fría y fruta picada', 20000, 7);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Sandwich', 'Emparedado con mortadela y pollo desmechado, lechuga, tomate y salsas', 15000, 7);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Waffles', 'Galleta crujiente y esponjosa acompañada con fruta y nutella', 18000, 7);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Café', '', 2500, 8);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Chocolate', '', 2500, 8);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Jugo de Naranja', '', 2500, 8);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Avena fría', '', 2500, 8);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Limonada', '', 2500, 8);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Leche fría', '', 2500, 8);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Yogur', '', 3500, 8);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Kumis casero', '', 4000, 8);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Chorizo', '', 4000, 9);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Salchicha', '', 2500, 9);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Queso', '', 4500, 9);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Cuajada', '', 3000, 9);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Aros de Cebolla', '', 4000, 9);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Rodajas de Tomate', '', 3000, 9);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Arepa de maíz blanco', '', 2500, 9);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Costilla', '', 5000, 9);
INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES ('Pan Ocañero', '', 2000, 9);

CREATE TABLE usuarios(
    iduser INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    nomus VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    rolus ENUM('cliente', 'administrador') NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE carrito(
    idprod INT,
    iduser INT,
    cantidad INT,
    total INT,
    CONSTRAINT fk_productos FOREIGN KEY (idprod) REFERENCES productos(idprod),
    CONSTRAINT fk_usuarios FOREIGN KEY (iduser) REFERENCES usuarios(iduser)
);