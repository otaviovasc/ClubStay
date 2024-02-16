class CreateCards < ActiveRecord::Migration[7.0]
  def change
    create_table :cards do |t|
      t.integer :number
      t.integer :cvc
      t.integer :exp_month
      t.integer :exp_year
      t.references :customer, null: false, foreign_key: true
      t.boolean :card_status
      t.string :stripe_id

      t.timestamps
    end
  end
end
