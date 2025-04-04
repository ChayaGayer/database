
-- Add NOT NULL constraint to Reviews.ReviewComment
ALTER TABLE Reviews
ALTER COLUMN ReviewComment SET NOT NULL;

-- Add CHECK constraint to Orders.TotalAmount to ensure it's always positive
ALTER TABLE Orders
ADD CONSTRAINT chk_total_amount_positive CHECK (TotalAmount > 0);

-- Add DEFAULT value to Dishes.Category
ALTER TABLE Delivers
ALTER COLUMN DeliveryStatus SET DEFAULT status1;
