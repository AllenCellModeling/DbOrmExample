from orator.migrations import Migration


class CreateIrenaClassificationsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('irena_classifications') as table:
            table.increments('id')
            table.timestamps()
            table.string('input_folder', 200)
            table.string('input_filename', 100)
            table.integer('output_cell_index').unsigned()
            table.string('cell_id', 20)
            table.integer('mitosis_label').unsigned()
            table.string('mitotic_handoff', 20)
            table.string('save_flat_reg_path', 300)
            table.string('save_flat_proj_reg_path', 300)
            table.string('save_h5_reg_path', 300)
            table.integer('png_file_size')
            table.integer('target_numeric')


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('irena_classifications')
