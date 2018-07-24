using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpeechToTextWPFSample
{
    public class Statement
    {
        public int id;

        public string statementValue;

        public long timeInSeconds;
    }

   public class Statements
    {
        public List<Statement> statements = new List<Statement>();
    }
}
