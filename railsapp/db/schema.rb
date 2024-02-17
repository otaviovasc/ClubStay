# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.0].define(version: 2024_02_16_185353) do
  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "cards", force: :cascade do |t|
    t.bigint "number"
    t.integer "cvc"
    t.integer "exp_month"
    t.integer "exp_year"
    t.bigint "customer_id", null: false
    t.boolean "card_status"
    t.string "stripe_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["customer_id"], name: "index_cards_on_customer_id"
  end

  create_table "customers", force: :cascade do |t|
    t.text "name"
    t.bigint "team_id", null: false
    t.string "email"
    t.integer "tempo_de_assinatura"
    t.integer "historico_de_presenca_nos_jogos"
    t.integer "historico_de_socio"
    t.integer "numero_de_desistencias_no_periodo"
    t.integer "historico_de_preco_nos_planos"
    t.string "tipo_de_plano"
    t.integer "quantos_membros"
    t.string "planos_com_ingresso_incluso"
    t.string "estado_civil"
    t.float "risco_de_churn"
    t.string "feedback_sobre_servicos"
    t.string "frequencia_de_compra_de_produtos"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["team_id"], name: "index_customers_on_team_id"
  end

  create_table "teams", force: :cascade do |t|
    t.text "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "users", force: :cascade do |t|
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
  end

  add_foreign_key "cards", "customers"
  add_foreign_key "customers", "teams"
end
