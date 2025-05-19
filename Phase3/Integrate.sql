-- === Step 1: Remove foreign key constraint ===
ALTER TABLE public.orders
DROP CONSTRAINT orders_deliveryid_fkey;

-- === Step 2: Update deliveryid values to prevent conflicts ===
UPDATE public.orders
SET deliveryid = deliveryid + 605
WHERE deliveryid IS NOT NULL;

UPDATE public.delivers
SET deliveryid = deliveryid + 605;

-- === Step 3: Re-add foreign key constraint ===
ALTER TABLE public.orders
ADD CONSTRAINT orders_deliveryid_fkey
FOREIGN KEY (deliveryid)
REFERENCES public.delivers (deliveryid);

-- === Step 4: Insert workers based on delivers table (NULL version) ===
INSERT INTO public.worker (
    wfirstname, wlastname, wid, salary, havebonus, wseniority, wstatus
)
SELECT 
    couriername, NULL, deliveryid, NULL, NULL, NULL, deliverystatus
FROM public.delivers
WHERE deliveryid NOT IN (SELECT wid FROM public.worker);

-- === Step 5: Insert workers based on delivers table (Default values version) ===
INSERT INTO public.worker (
    wfirstname, wlastname, wid, salary, havebonus, wseniority, wstatus
)
SELECT 
    couriername, '', deliveryid, 0, 0, 0, deliverystatus
FROM public.delivers
WHERE deliveryid NOT IN (SELECT wid FROM public.worker);



-- === Step 7: Insert data from meal into dishes ===
INSERT INTO public.dishes (
    dishid, dishname, description, price, category, mname, mprice
)
SELECT 
    mid, mname, 'Imported from meal table', mprice::numeric(10,2), 'Meal', mname, mprice
FROM public.meal
WHERE mid NOT IN (SELECT dishid FROM public.dishes WHERE dishid IS NOT NULL);

-- === Step 8: Update existing dishes from meal ===
UPDATE public.dishes 
SET 
    mname = m.mname,
    mprice = m.mprice,
    dishname = m.mname,
    price = m.mprice::numeric(10,2)
FROM public.meal m
WHERE dishes.dishid = m.mid;

-- === Step 9: Check final results ===
SELECT 
    dishid, dishname, mname, price, mprice, category, description
FROM public.dishes
ORDER BY dishid;


ALTER TABLE public.dishes
DROP COLUMN mname,
DROP COLUMN mprice;

ALTER TABLE delivers 
DROP COLUMN couriername,
DROP COLUMN deliverystatus;
