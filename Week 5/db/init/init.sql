CREATE TABLE IF NOT EXISTS Meals (
    MealId SERIAL PRIMARY KEY
    ,MealName TEXT NOT NULL
    ,MealPrice REAL NOT NULL
);

INSERT INTO Meals(MealName, MealPrice) VALUES ('Margherita pizza', 24.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Speghetti pasta', 26.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Anti-pasta', 28.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Bruscheta', 22.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Caesar salad', 27.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('MUSHROOM RAVIOLI AL FORNO', 22.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('SHRIMP SCAMPI', 22.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('LOBSTER CREAM SAUCE', 23.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('CHICKEN MARSALA', 24.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('CHICKEN PARMESAN', 28.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Risotto', 22.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Gnocchi', 22.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Pesto alla Genovese', 23.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('lasagne', 28.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('SPAGHETTI & MEATBALL', 28.99);