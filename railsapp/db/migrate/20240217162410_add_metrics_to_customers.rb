class AddMetricsToCustomers < ActiveRecord::Migration[7.0]
  def change
    add_column :customers, :ltv, :float
    add_column :customers, :cac, :float
    add_column :customers, :expected_payments, :float
    add_column :customers, :roi, :float
    add_column :customers, :investment_mkt, :float
  end
end
