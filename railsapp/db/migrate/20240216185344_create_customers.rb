class CreateCustomers < ActiveRecord::Migration[7.0]
  def change
    create_table :customers do |t|
      t.text :name
      t.references :team, foreign_key: true

      t.timestamps
    end
  end
end
